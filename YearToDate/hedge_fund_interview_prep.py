import pandas as pd
import numpy as np
from datetime import datetime, timedelta

class HedgeFundDataProcessor:
    """
    A comprehensive solution for processing hedge fund data and calculating returns.
    This demonstrates pandas proficiency and financial data analysis skills.
    """
    
    def __init__(self):
        self.portfolio_data = None
        self.benchmark_data = None
        self.risk_free_rate = 0.02  # 2% annual risk-free rate
        
    def generate_sample_data(self, start_date='2024-01-01', end_date='2024-12-31'):
        """
        Generate realistic sample data for a hedge fund portfolio and benchmark.
        """
        # Create date range
        date_range = pd.date_range(start=start_date, end=end_date, freq='D')
        
        # Generate portfolio data
        np.random.seed(42)  # For reproducible results
        
        # Simulate daily returns with some volatility clustering
        daily_returns = np.random.normal(0.0008, 0.015, len(date_range))  # 0.08% daily mean, 1.5% volatility
        
        # Add some market stress periods
        stress_periods = [50, 150, 250, 350]
        for period in stress_periods:
            if period < len(daily_returns):
                daily_returns[period:period+10] *= -0.5  # Negative returns during stress
        
        # Calculate cumulative returns
        cumulative_returns = (1 + daily_returns).cumprod()
        
        # Create portfolio data
        portfolio_data = pd.DataFrame({
            'date': date_range,
            'daily_return': daily_returns,
            'cumulative_return': cumulative_returns,
            'nav': 1000 * cumulative_returns,  # Starting NAV of $1000
            'volume': np.random.randint(1000, 10000, len(date_range)),
            'volatility': np.random.uniform(0.01, 0.03, len(date_range))
        })
        
        # Generate benchmark data (S&P 500-like)
        benchmark_returns = np.random.normal(0.0006, 0.012, len(date_range))
        benchmark_cumulative = (1 + benchmark_returns).cumprod()
        
        benchmark_data = pd.DataFrame({
            'date': date_range,
            'daily_return': benchmark_returns,
            'cumulative_return': benchmark_cumulative,
            'nav': 1000 * benchmark_cumulative
        })
        
        # Add some missing data to handle real-world scenarios
        portfolio_data.loc[portfolio_data.sample(frac=0.02).index, 'nav'] = np.nan
        portfolio_data.loc[portfolio_data.sample(frac=0.01).index, 'daily_return'] = np.nan
        
        self.portfolio_data = portfolio_data
        self.benchmark_data = benchmark_data
        
        return portfolio_data, benchmark_data
    
    def clean_data(self):
        """
        Clean the data by handling missing values and outliers.
        """
        if self.portfolio_data is None:
            raise ValueError("No data loaded. Call generate_sample_data() first.")
        
        # Forward fill missing NAV values
        self.portfolio_data['nav'] = self.portfolio_data['nav'].fillna(method='ffill')
        
        # For missing daily returns, calculate from NAV
        mask = self.portfolio_data['daily_return'].isna()
        self.portfolio_data.loc[mask, 'daily_return'] = (
            self.portfolio_data.loc[mask, 'nav'] / 
            self.portfolio_data.loc[mask, 'nav'].shift(1) - 1
        )
        
        # Remove any remaining NaN values
        self.portfolio_data = self.portfolio_data.dropna()
        
        return self.portfolio_data
    
    def calculate_ytd_return(self, as_of_date=None):
        """
        Calculate year-to-date return for the portfolio for a specific date.
        """
        if self.portfolio_data is None:
            raise ValueError("No data loaded. Call generate_sample_data() first.")
        
        if as_of_date is None:
            as_of_date = self.portfolio_data['date'].max()
        
        # Get the first day of the year
        year_start = pd.Timestamp(as_of_date.year, 1, 1)
        
        # Get NAV at year start and current date
        year_start_nav = self.portfolio_data[
            self.portfolio_data['date'] >= year_start
        ]['nav'].iloc[0]
        
        current_nav = self.portfolio_data[
            self.portfolio_data['date'] <= as_of_date
        ]['nav'].iloc[-1]
        
        ytd_return = (current_nav / year_start_nav) - 1
        
        return {
            'ytd_return': ytd_return,
            'ytd_return_pct': ytd_return * 100,
            'year_start_nav': year_start_nav,
            'current_nav': current_nav,
            'as_of_date': as_of_date
        }
    
    def calculate_ytd_returns_series(self, frequency='M'):
        """
        Calculate year-to-date returns for the entire dataset at specified frequency.
        
        Parameters:
        - frequency: 'M' for monthly, 'Q' for quarterly, 'W' for weekly, 'D' for daily
        
        Returns:
        - DataFrame with YTD returns for each period
        """
        if self.portfolio_data is None:
            raise ValueError("No data loaded. Call generate_sample_data() first.")
        
        # Create a copy of the data and sort by date
        data = self.portfolio_data.copy().sort_values('date')
        
        # Resample to the specified frequency and get the last NAV of each period
        resampled = data.set_index('date')['nav'].resample(frequency).last().dropna()
        
        # Get year start NAVs for each year
        # year_start_navs = data.groupby(data['date'].dt.year)['nav'].last().shift(1, fill_value=0)
        year_start_navs = data.groupby(pd.Grouper(key='date', freq='Y'))['nav'].last().shift(1, fill_value=0)
        
        # Create a DataFrame with resampled NAVs and add year column
        result_df = resampled.reset_index()
        result_df['year'] = result_df['date'].dt.year
        
        # Map year start NAVs to each row
        result_df['year_start_nav'] = result_df['year'].map(year_start_navs)
        
        # Calculate YTD returns vectorized
        result_df['ytd_return'] = (result_df['nav'] / result_df['year_start_nav']) - 1
        result_df['ytd_return_pct'] = result_df['ytd_return'] * 100
        
        return result_df
    
    def calculate_rolling_ytd_returns(self, window_days=252):
        """
        Calculate rolling year-to-date returns using a rolling window.
        This is useful for analyzing YTD performance over time.
        
        Parameters:
        - window_days: Number of days in the rolling window (default: 252 trading days)
        
        Returns:
        - DataFrame with rolling YTD returns
        """
        if self.portfolio_data is None:
            raise ValueError("No data loaded. Call generate_sample_data() first.")
        
        data = self.portfolio_data.copy().sort_values('date')
        
        rolling_ytd = []
        
        for i in range(window_days, len(data)):
            # Get the window of data
            window_data = data.iloc[i-window_days:i+1]
            
            # Calculate YTD return for the end of this window
            end_date = window_data['date'].iloc[-1]
            year_start = pd.Timestamp(end_date.year, 1, 1)
            
            # Get NAV at year start
            year_start_nav = data[data['date'] >= year_start]['nav'].iloc[0]
            current_nav = window_data['nav'].iloc[-1]
            
            ytd_return = (current_nav / year_start_nav) - 1
            
            rolling_ytd.append({
                'date': end_date,
                'nav': current_nav,
                'year_start_nav': year_start_nav,
                'ytd_return': ytd_return,
                'ytd_return_pct': ytd_return * 100,
                'year': end_date.year
            })
        
        return pd.DataFrame(rolling_ytd)
    
    def calculate_ytd_by_year(self):
        """
        Calculate year-to-date returns for each year in the dataset.
        Returns a summary by year.
        """
        if self.portfolio_data is None:
            raise ValueError("No data loaded. Call generate_sample_data() first.")
        
        data = self.portfolio_data.copy().sort_values('date')
        
        # Group by year
        yearly_summary = []
        
        for year in data['date'].dt.year.unique():
            year_data = data[data['date'].dt.year == year]
            
            if len(year_data) > 0:
                year_start_nav = year_data['nav'].iloc[0]
                year_end_nav = year_data['nav'].iloc[-1]
                year_end_date = year_data['date'].iloc[-1]
                
                ytd_return = (year_end_nav / year_start_nav) - 1
                
                yearly_summary.append({
                    'year': year,
                    'start_date': year_data['date'].iloc[0],
                    'end_date': year_end_date,
                    'year_start_nav': year_start_nav,
                    'year_end_nav': year_end_nav,
                    'ytd_return': ytd_return,
                    'ytd_return_pct': ytd_return * 100,
                    'trading_days': len(year_data)
                })
        
        return pd.DataFrame(yearly_summary)
    
    def calculate_rolling_metrics(self, window=30):
        """
        Calculate rolling metrics like volatility, Sharpe ratio, and drawdown.
        """
        if self.portfolio_data is None:
            raise ValueError("No data loaded. Call generate_sample_data() first.")
        
        # Rolling volatility (annualized)
        rolling_vol = self.portfolio_data['daily_return'].rolling(window=window).std() * np.sqrt(252)
        
        # Rolling Sharpe ratio
        rolling_return = self.portfolio_data['daily_return'].rolling(window=window).mean() * 252
        rolling_sharpe = (rolling_return - self.risk_free_rate) / rolling_vol
        
        # Rolling maximum (for drawdown calculation)
        rolling_max = self.portfolio_data['nav'].rolling(window=window, min_periods=1).max()
        drawdown = (self.portfolio_data['nav'] - rolling_max) / rolling_max
        
        # Add to portfolio data
        self.portfolio_data['rolling_volatility'] = rolling_vol
        self.portfolio_data['rolling_sharpe'] = rolling_sharpe
        self.portfolio_data['drawdown'] = drawdown
        
        return self.portfolio_data
    
    def calculate_risk_metrics(self):
        """
        Calculate comprehensive risk metrics for the portfolio.
        """
        if self.portfolio_data is None:
            raise ValueError("No data loaded. Call generate_sample_data() first.")
        
        returns = self.portfolio_data['daily_return']
        
        # Basic metrics
        total_return = (self.portfolio_data['nav'].iloc[-1] / self.portfolio_data['nav'].iloc[0]) - 1
        annualized_return = (1 + total_return) ** (252 / len(returns)) - 1
        volatility = returns.std() * np.sqrt(252)
        sharpe_ratio = (annualized_return - self.risk_free_rate) / volatility
        
        # Maximum drawdown
        cumulative_returns = (1 + returns).cumprod()
        running_max = cumulative_returns.expanding().max()
        drawdown = (cumulative_returns - running_max) / running_max
        max_drawdown = drawdown.min()
        
        # VaR and CVaR (95% confidence)
        var_95 = np.percentile(returns, 5)
        cvar_95 = returns[returns <= var_95].mean()
        
        # Skewness and kurtosis
        skewness = returns.skew()
        kurtosis = returns.kurtosis()
        
        return {
            'total_return': total_return,
            'annualized_return': annualized_return,
            'volatility': volatility,
            'sharpe_ratio': sharpe_ratio,
            'max_drawdown': max_drawdown,
            'var_95': var_95,
            'cvar_95': cvar_95,
            'skewness': skewness,
            'kurtosis': kurtosis
        }
    
    def compare_with_benchmark(self):
        """
        Compare portfolio performance with benchmark.
        """
        if self.portfolio_data is None or self.benchmark_data is None:
            raise ValueError("Both portfolio and benchmark data required.")
        
        # Merge data on date
        comparison = pd.merge(
            self.portfolio_data[['date', 'daily_return', 'nav']],
            self.benchmark_data[['date', 'daily_return', 'nav']],
            on='date',
            suffixes=('_portfolio', '_benchmark')
        )
        
        # Calculate excess returns
        comparison['excess_return'] = comparison['daily_return_portfolio'] - comparison['daily_return_benchmark']
        
        # Calculate tracking error
        tracking_error = comparison['excess_return'].std() * np.sqrt(252)
        
        # Calculate information ratio
        excess_return_mean = comparison['excess_return'].mean() * 252
        information_ratio = excess_return_mean / tracking_error
        
        # Calculate beta
        covariance = np.cov(comparison['daily_return_portfolio'], comparison['daily_return_benchmark'])[0, 1]
        benchmark_variance = comparison['daily_return_benchmark'].var()
        beta = covariance / benchmark_variance
        
        # Calculate alpha
        portfolio_return = comparison['daily_return_portfolio'].mean() * 252
        benchmark_return = comparison['daily_return_benchmark'].mean() * 252
        alpha = portfolio_return - (self.risk_free_rate + beta * (benchmark_return - self.risk_free_rate))
        
        return {
            'tracking_error': tracking_error,
            'information_ratio': information_ratio,
            'beta': beta,
            'alpha': alpha,
            'excess_return_mean': excess_return_mean
        }
    
    def generate_report(self):
        """
        Generate a comprehensive performance report.
        """
        if self.portfolio_data is None:
            raise ValueError("No data loaded. Call generate_sample_data() first.")
        
        # Clean data first
        self.clean_data()
        
        # Calculate all metrics
        ytd_metrics = self.calculate_ytd_return()
        risk_metrics = self.calculate_risk_metrics()
        
        # Calculate rolling metrics
        self.calculate_rolling_metrics()
        
        # Compare with benchmark if available
        benchmark_comparison = {}
        if self.benchmark_data is not None:
            benchmark_comparison = self.compare_with_benchmark()
        
        # Create summary report
        report = {
            'portfolio_summary': {
                'start_date': self.portfolio_data['date'].min(),
                'end_date': self.portfolio_data['date'].max(),
                'total_days': len(self.portfolio_data),
                'initial_nav': self.portfolio_data['nav'].iloc[0],
                'final_nav': self.portfolio_data['nav'].iloc[-1]
            },
            'ytd_performance': ytd_metrics,
            'risk_metrics': risk_metrics,
            'benchmark_comparison': benchmark_comparison
        }
        
        return report
    



def main():
    """
    Main function demonstrating the hedge fund data processing capabilities.
    """
    print("=== Hedge Fund Interview Preparation ===\n")
    
    # Initialize processor
    processor = HedgeFundDataProcessor()
    
    # Generate sample data with multiple years
    print("1. Generating sample financial data (multiple years)...")
    portfolio_data, benchmark_data = processor.generate_sample_data(start_date='2022-01-01', end_date='2024-12-31')
    print(f"   Generated {len(portfolio_data)} days of portfolio data")
    print(f"   Generated {len(benchmark_data)} days of benchmark data")
    print(f"   Date range: {portfolio_data['date'].min().strftime('%Y-%m-%d')} to {portfolio_data['date'].max().strftime('%Y-%m-%d')}")
    
    # Clean data
    print("\n2. Cleaning data...")
    cleaned_data = processor.clean_data()
    print(f"   Data cleaned successfully")
    
    # Calculate YTD return for current date
    print("\n3. Calculating year-to-date return for current date...")
    ytd_metrics = processor.calculate_ytd_return()
    print(f"   Current YTD Return: {ytd_metrics['ytd_return_pct']:.2f}%")
    print(f"   Year Start NAV: ${ytd_metrics['year_start_nav']:.2f}")
    print(f"   Current NAV: ${ytd_metrics['current_nav']:.2f}")
    
    # Calculate YTD returns series (monthly)
    print("\n4. Calculating YTD returns for each month...")
    ytd_series = processor.calculate_ytd_returns_series(frequency='M')
    print(f"   Generated YTD returns for {len(ytd_series)} months")
    print("   Sample monthly YTD returns:")
    print(ytd_series[['date', 'ytd_return_pct']].head(10).to_string(index=False))
    
    # Calculate YTD returns by year
    print("\n5. Calculating YTD returns by year...")
    ytd_by_year = processor.calculate_ytd_by_year()
    print("   YTD returns by year:")
    print(ytd_by_year[['year', 'ytd_return_pct', 'trading_days']].to_string(index=False))
    
    # Calculate risk metrics
    print("\n6. Calculating risk metrics...")
    risk_metrics = processor.calculate_risk_metrics()
    print(f"   Annualized Return: {risk_metrics['annualized_return']*100:.2f}%")
    print(f"   Volatility: {risk_metrics['volatility']*100:.2f}%")
    print(f"   Sharpe Ratio: {risk_metrics['sharpe_ratio']:.2f}")
    print(f"   Maximum Drawdown: {risk_metrics['max_drawdown']*100:.2f}%")
    
    # Compare with benchmark
    print("\n7. Comparing with benchmark...")
    benchmark_comparison = processor.compare_with_benchmark()
    print(f"   Beta: {benchmark_comparison['beta']:.2f}")
    print(f"   Alpha: {benchmark_comparison['alpha']*100:.2f}%")
    print(f"   Information Ratio: {benchmark_comparison['information_ratio']:.2f}")
    
    # Generate comprehensive report
    print("\n8. Generating comprehensive report...")
    report = processor.generate_report()
    
    print("\n=== COMPREHENSIVE PERFORMANCE REPORT ===")
    print(f"Analysis Period: {report['portfolio_summary']['start_date'].strftime('%Y-%m-%d')} to {report['portfolio_summary']['end_date'].strftime('%Y-%m-%d')}")
    print(f"Total Days: {report['portfolio_summary']['total_days']}")
    print(f"Initial NAV: ${report['portfolio_summary']['initial_nav']:.2f}")
    print(f"Final NAV: ${report['portfolio_summary']['final_nav']:.2f}")
    print(f"YTD Return: {report['ytd_performance']['ytd_return_pct']:.2f}%")
    print(f"Annualized Return: {report['risk_metrics']['annualized_return']*100:.2f}%")
    print(f"Volatility: {report['risk_metrics']['volatility']*100:.2f}%")
    print(f"Sharpe Ratio: {report['risk_metrics']['sharpe_ratio']:.2f}")
    print(f"Maximum Drawdown: {report['risk_metrics']['max_drawdown']*100:.2f}%")
    print(f"Beta: {report['benchmark_comparison']['beta']:.2f}")
    print(f"Alpha: {report['benchmark_comparison']['alpha']*100:.2f}%")
    

    
    print("\n=== Interview Preparation Complete ===")
    print("This demonstrates proficiency in:")
    print("- Pandas data manipulation and analysis")
    print("- Financial data processing and cleaning")
    print("- Risk metrics calculation")
    print("- Performance attribution analysis")
    print("- Object-oriented programming")
    print("- Multi-year YTD return analysis")


if __name__ == "__main__":
    main() 