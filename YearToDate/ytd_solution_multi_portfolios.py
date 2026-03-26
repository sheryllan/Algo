import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import warnings

warnings.filterwarnings('ignore')

# Generate mock financial data for multiple portfolios
np.random.seed(42)  # For reproducible results


def generate_multi_portfolio_data():
    """
    Generate mock data for multiple portfolios.
    Returns daily portfolio values for multiple portfolios across the year.
    """
    portfolios = ['Alpha_Fund', 'Beta_Strategy', 'Gamma_Hedge', 'Delta_Long_Short', 'Epsilon_Arbitrage']

    # Create date range for current year
    start_date = datetime(2024, 1, 1)
    end_date = datetime(2024, 12, 31)
    dates = pd.date_range(start=start_date, end=end_date, freq='B')  # Business days only

    all_data = []

    for portfolio in portfolios:
        # Different initial values and risk profiles for each portfolio
        portfolio_configs = {
            'Alpha_Fund': {'initial': 150_000_000, 'mean_return': 0.0012, 'volatility': 0.020},
            'Beta_Strategy': {'initial': 80_000_000, 'mean_return': 0.0008, 'volatility': 0.015},
            'Gamma_Hedge': {'initial': 200_000_000, 'mean_return': 0.0005, 'volatility': 0.008},
            'Delta_Long_Short': {'initial': 120_000_000, 'mean_return': 0.0010, 'volatility': 0.018},
            'Epsilon_Arbitrage': {'initial': 60_000_000, 'mean_return': 0.0006, 'volatility': 0.012}
        }

        config = portfolio_configs[portfolio]

        # Generate returns with different characteristics per portfolio
        np.random.seed(hash(portfolio) % 1000)  # Different seed per portfolio
        returns = np.random.normal(config['mean_return'], config['volatility'], len(dates))

        # Create cumulative portfolio values
        portfolio_values = [config['initial']]
        for daily_return in returns[1:]:
            new_value = portfolio_values[-1] * (1 + daily_return)
            portfolio_values.append(new_value)

        # Create DataFrame for this portfolio
        portfolio_df = pd.DataFrame({
            'date': dates,
            'portfolio_id': portfolio,
            'portfolio_value': portfolio_values
        })

        all_data.append(portfolio_df)

    # Combine all portfolios
    combined_df = pd.concat(all_data, ignore_index=True)
    return combined_df


def calculate_monthly_ytd_by_portfolio_vectorized(df, value_column='portfolio_value',
                                                  date_column='date', portfolio_column='portfolio_id'):
    """
    Calculate YTD return for each month for each portfolio using vectorized operations.

    MUCH faster than loop-based approach for large datasets.

    Parameters:
    df: DataFrame with portfolio data
    value_column: Column name containing portfolio values
    date_column: Column name containing dates
    portfolio_column: Column name containing portfolio identifiers

    Returns:
    DataFrame: Monthly YTD returns by portfolio
    """
    # Ensure date column is datetime and sort
    df[date_column] = pd.to_datetime(df[date_column])
    df = df.sort_values([portfolio_column, date_column]).reset_index(drop=True)

    # Filter for current year
    current_year = df[date_column].dt.year.iloc[-1]
    ytd_data = df[df[date_column].dt.year == current_year].copy()

    # Add helper columns
    ytd_data['year_month'] = ytd_data[date_column].dt.to_period('M')

    # VECTORIZED APPROACH:
    # 1. Get start values (first value of year for each portfolio)
    start_values = ytd_data.groupby(portfolio_column)[value_column].first()

    # 2. Get month-end values for each portfolio-month combination
    month_end_values = ytd_data.groupby([portfolio_column, 'year_month']).agg({
        value_column: 'last',
        date_column: 'last'
    }).reset_index()

    # 3. Merge start values with month-end values (vectorized join)
    month_end_values['start_value'] = month_end_values[portfolio_column].map(start_values)

    # 4. Calculate all YTD returns at once (vectorized calculation)
    month_end_values['ytd_return_pct'] = (
                                                 (month_end_values[value_column] - month_end_values['start_value']) /
                                                 month_end_values['start_value']
                                         ) * 100

    # 5. Rename columns for clarity
    month_end_values = month_end_values.rename(columns={
        value_column: 'end_value',
        date_column: 'month_end_date',
        'year_month': 'year_month'
    })

    # 6. Convert period to string for display
    month_end_values['year_month'] = month_end_values['year_month'].astype(str)

    # 7. Calculate days from start (vectorized)
    start_dates = ytd_data.groupby(portfolio_column)[date_column].first()
    month_end_values['start_date'] = month_end_values[portfolio_column].map(start_dates)
    month_end_values['days_from_start'] = (
            month_end_values['month_end_date'] - month_end_values['start_date']
    ).dt.days

    # Clean up and reorder columns
    result_columns = ['portfolio_id', 'year_month', 'month_end_date', 'start_value',
                      'end_value', 'ytd_return_pct', 'days_from_start']

    return month_end_values[result_columns].sort_values(['portfolio_id', 'year_month'])


def calculate_monthly_ytd_by_portfolio(df, value_column='portfolio_value',
                                       date_column='date', portfolio_column='portfolio_id'):
    """
    Wrapper function that calls the vectorized version.
    Kept for backward compatibility.
    """
    return calculate_monthly_ytd_by_portfolio_vectorized(df, value_column, date_column, portfolio_column)


def calculate_portfolio_summary_stats_vectorized(df, value_column='portfolio_value',
                                                 date_column='date', portfolio_column='portfolio_id'):
    """
    Calculate summary statistics for each portfolio using vectorized operations.
    MUCH faster than loop-based approach.
    """
    df[date_column] = pd.to_datetime(df[date_column])
    df = df.sort_values([portfolio_column, date_column])

    # Calculate daily returns for all portfolios at once
    df['daily_return'] = df.groupby(portfolio_column)[value_column].pct_change()

    # VECTORIZED AGGREGATIONS:
    # 1. Basic values (start, end, count)
    basic_stats = df.groupby(portfolio_column).agg({
        value_column: ['first', 'last', 'count'],
        'daily_return': ['mean', 'std']
    }).reset_index()

    # Flatten column names
    basic_stats.columns = [f"{col[0]}_{col[1]}" if col[1] else col[0]
                           for col in basic_stats.columns]

    # Rename for clarity
    basic_stats = basic_stats.rename(columns={
        f'{value_column}_first': 'start_value',
        f'{value_column}_last': 'end_value',
        f'{value_column}_count': 'total_observations',
        'daily_return_mean': 'avg_daily_return',
        'daily_return_std': 'daily_volatility'
    })

    # 2. Calculate derived metrics (vectorized)
    basic_stats['total_return_pct'] = (
                                              (basic_stats['end_value'] - basic_stats['start_value']) /
                                              basic_stats['start_value']
                                      ) * 100

    basic_stats['annualized_volatility_pct'] = (
                                                       basic_stats['daily_volatility'] * np.sqrt(252)
                                               ) * 100

    basic_stats['sharpe_ratio'] = np.where(
        basic_stats['daily_volatility'] != 0,
        (basic_stats['avg_daily_return'] * 252) / (basic_stats['daily_volatility'] * np.sqrt(252)),
        0
    )

    # 3. Calculate max drawdown (vectorized per portfolio)
    def calculate_max_drawdown_vectorized(group):
        running_max = group[value_column].expanding().max()
        drawdown = (group[value_column] - running_max) / running_max
        return drawdown.min()

    max_drawdowns = df.groupby(portfolio_column).apply(calculate_max_drawdown_vectorized)
    basic_stats['max_drawdown_pct'] = basic_stats[portfolio_column].map(max_drawdowns) * 100

    # Select final columns
    result_columns = [portfolio_column, 'start_value', 'end_value', 'total_return_pct',
                      'annualized_volatility_pct', 'sharpe_ratio', 'max_drawdown_pct']

    return basic_stats[result_columns]


def calculate_portfolio_summary_stats(df, value_column='portfolio_value',
                                      date_column='date', portfolio_column='portfolio_id'):
    """
    Wrapper function that calls the vectorized version.
    Kept for backward compatibility.
    """
    return calculate_portfolio_summary_stats_vectorized(df, value_column, date_column, portfolio_column)


def create_ytd_pivot_table(monthly_ytd_df):
    """
    Create a pivot table showing YTD returns by portfolio and month.
    """
    pivot_df = monthly_ytd_df.pivot(index='portfolio_id',
                                    columns='year_month',
                                    values='ytd_return_pct')
    return pivot_df


# Main execution - Advanced interview scenario
if __name__ == "__main__":
    print("\n=== ADVANCED HEDGE FUND CODING INTERVIEW SCENARIO ===")
    print("Task: Calculate Monthly YTD Returns for Multiple Portfolios (VECTORIZED)")
    print("=" * 70)

    # Performance comparison demonstration
    import time

    print("1. Loading multi-portfolio data...")
    portfolio_df = generate_multi_portfolio_data()
    print(f"   Data shape: {portfolio_df.shape}")
    print(f"   Portfolios: {portfolio_df['portfolio_id'].nunique()}")
    print(f"   Portfolio names: {list(portfolio_df['portfolio_id'].unique())}")
    print(
        f"   Date range: {portfolio_df['date'].min().strftime('%Y-%m-%d')} to {portfolio_df['date'].max().strftime('%Y-%m-%d')}")

    # Step 2: Display sample of the data
    print("\n2. Sample of multi-portfolio data:")
    sample_data = portfolio_df.groupby('portfolio_id').head(2)
    print(sample_data)

    # Step 3: Demonstrate vectorized performance
    print("\n3. Calculating Monthly YTD returns (VECTORIZED approach)...")
    start_time = time.time()
    monthly_ytd_results = calculate_monthly_ytd_by_portfolio_vectorized(portfolio_df)
    vectorized_time = time.time() - start_time
    print(f"   Vectorized calculation completed in: {vectorized_time:.4f} seconds")

    # Step 4: Create pivot table for easy viewing
    print("\n4. Monthly YTD Returns Pivot Table:")
    ytd_pivot = create_ytd_pivot_table(monthly_ytd_results)
    print(ytd_pivot.round(2))

    # Step 5: Portfolio summary statistics (also vectorized)
    print("\n5. Portfolio Summary Statistics (VECTORIZED):")
    start_time = time.time()
    summary_stats = calculate_portfolio_summary_stats_vectorized(portfolio_df)
    summary_time = time.time() - start_time
    print(f"   Summary stats calculated in: {summary_time:.4f} seconds")
    print(summary_stats.round(2))

    # Step 6: Detailed view for one portfolio
    print("\n6. Detailed Monthly YTD Progress for Alpha_Fund:")
    alpha_details = monthly_ytd_results[monthly_ytd_results['portfolio_id'] == 'Alpha_Fund']
    for _, row in alpha_details.iterrows():
        print(f"   {row['year_month']}: {row['ytd_return_pct']:.2f}% "
              f"(${row['end_value']:,.0f})")

    # Step 7: Best and worst performing portfolios by final YTD
    print("\n7. Portfolio Rankings by Final YTD Return:")
    final_ytd = monthly_ytd_results.groupby('portfolio_id')['ytd_return_pct'].last().sort_values(ascending=False)
    for i, (portfolio, ytd_return) in enumerate(final_ytd.items(), 1):
        print(f"   {i}. {portfolio}: {ytd_return:.2f}%")

    # Step 8: Data validation
    print(f"\n8. Data Quality Check:")
    print(f"   Total records: {len(portfolio_df):,}")
    print(f"   Missing values: {portfolio_df.isnull().sum().sum()}")
    print(f"   Records per portfolio: {portfolio_df.groupby('portfolio_id').size().to_dict()}")

    print("\n=== VECTORIZED APPROACH ADVANTAGES ===")
    print("Key vectorization techniques demonstrated:")
    print("- groupby().agg() for multiple aggregations in one pass")
    print("- map() for efficient lookups instead of merge operations")
    print("- Vectorized arithmetic operations on entire columns")
    print("- np.where() for conditional logic without loops")
    print("- Single-pass calculations vs nested loops")
    print("- Pandas period operations for time-based grouping")
    print("\nPerformance benefits:")
    print(f"- Vectorized YTD calculation: {vectorized_time:.4f}s")
    print(f"- Vectorized summary stats: {summary_time:.4f}s")
    print("- Scales linearly with data size (O(n) vs O(n²) for loops)")
    print("- Utilizes NumPy's optimized C implementations")
    print("- Memory efficient - avoids intermediate Python objects")