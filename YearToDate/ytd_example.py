#!/usr/bin/env python3
"""
Example script demonstrating the enhanced YTD calculation methods.
This shows how to calculate YTD returns for multiple years and different frequencies.
"""

import pandas as pd
import numpy as np
from hedge_fund_interview_prep import HedgeFundDataProcessor

def main():
    print("=== YTD Calculation Examples ===\n")
    
    # Initialize processor
    processor = HedgeFundDataProcessor()
    
    # Generate 3 years of data
    print("1. Generating 3 years of sample data...")
    portfolio_data, benchmark_data = processor.generate_sample_data(
        start_date='2022-01-01', 
        end_date='2024-12-31'
    )
    print(f"   Data range: {portfolio_data['date'].min().strftime('%Y-%m-%d')} to {portfolio_data['date'].max().strftime('%Y-%m-%d')}")
    print(f"   Total days: {len(portfolio_data)}")
    
    # Clean the data
    processor.clean_data()
    
    print("\n2. Calculating YTD returns for different frequencies...")
    
    # Monthly YTD returns
    monthly_ytd = processor.calculate_ytd_returns_series(frequency='M')
    print(f"\n   Monthly YTD returns (first 12 months):")
    print(monthly_ytd[['date', 'ytd_return_pct']].head(12).to_string(index=False))
    
    # Quarterly YTD returns
    quarterly_ytd = processor.calculate_ytd_returns_series(frequency='Q')
    print(f"\n   Quarterly YTD returns:")
    print(quarterly_ytd[['date', 'ytd_return_pct']].to_string(index=False))
    
    # Weekly YTD returns (sample)
    weekly_ytd = processor.calculate_ytd_returns_series(frequency='W')
    print(f"\n   Weekly YTD returns (first 20 weeks):")
    print(weekly_ytd[['date', 'ytd_return_pct']].head(20).to_string(index=False))
    
    print("\n3. YTD returns by year...")
    yearly_ytd = processor.calculate_ytd_by_year()
    print(yearly_ytd[['year', 'ytd_return_pct', 'trading_days']].to_string(index=False))
    
    print("\n4. Rolling YTD returns (252-day window)...")
    rolling_ytd = processor.calculate_rolling_ytd_returns(window_days=252)
    print(f"   Generated {len(rolling_ytd)} rolling YTD calculations")
    print("   Sample rolling YTD returns:")
    print(rolling_ytd[['date', 'ytd_return_pct']].head(10).to_string(index=False))
    
    print("\n5. Analysis insights...")
    
    # Find best and worst YTD months
    best_month = monthly_ytd.loc[monthly_ytd['ytd_return_pct'].idxmax()]
    worst_month = monthly_ytd.loc[monthly_ytd['ytd_return_pct'].idxmin()]
    
    print(f"   Best YTD month: {best_month['date'].strftime('%Y-%m')} with {best_month['ytd_return_pct']:.2f}%")
    print(f"   Worst YTD month: {worst_month['date'].strftime('%Y-%m')} with {worst_month['ytd_return_pct']:.2f}%")
    
    # Calculate average YTD by year
    avg_ytd_by_year = monthly_ytd.groupby('year')['ytd_return_pct'].mean()
    print(f"\n   Average YTD return by year:")
    for year, avg_ytd in avg_ytd_by_year.items():
        print(f"      {year}: {avg_ytd:.2f}%")
    
    # Calculate YTD volatility by year
    ytd_vol_by_year = monthly_ytd.groupby('year')['ytd_return_pct'].std()
    print(f"\n   YTD return volatility by year:")
    for year, ytd_vol in ytd_vol_by_year.items():
        print(f"      {year}: {ytd_vol:.2f}%")
    
    print("\n=== Example Complete ===")
    print("This demonstrates:")
    print("- Multi-year YTD calculation")
    print("- Different frequency resampling (M, Q, W)")
    print("- Rolling YTD analysis")
    print("- Year-by-year performance comparison")
    print("- Statistical analysis of YTD returns")

if __name__ == "__main__":
    main() 