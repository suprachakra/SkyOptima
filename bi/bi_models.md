## Business Intelligence Models

This document outlines the BI models integrated into SkyOptima for in-depth revenue and performance analysis.

### Core BI Metrics
- **Revenue per Available Seat Kilometer (PRASK):**  
  - Calculated using the formula:  
    $$ PRASK = \frac{TotalRevenue}{AvailableSeatKm} $$
  - Integrated into real-time dashboards for performance monitoring.
  
- **Forecast Accuracy:**  
  - Measured as Mean Absolute Percentage Error (MAPE) across multiple dimensions (Class, Departure Time, Day, Origin, Destination).

- **Dynamic Pricing Response Time:**  
  - Monitored through API latency metrics and system response metrics.
  
### Data Models
- **Historical Revenue Analysis Model:**  
  - Uses time series data from processed revenue data with ARIMA forecasts.
- **Customer Loyalty Impact Model:**  
  - Aggregates loyalty scores from Etihad Guest data to generate a “LoyaltyIndex.”
- **Dynamic Pricing Model:**  
  - Ensemble of ARIMA, LSTM, XGBoost, and reinforcement learning outputs for pricing optimization.
  
### Integration with BI Tools
- **Dashboard Layer:**  
  - Data from the BI models is fed into Tableau and Power BI dashboards.
- **Real-Time Data Feeds:**  
  - APIs deliver up-to-the-minute metrics to the BI layer for continuous monitoring.
  
## Reporting and Analysis
- **Performance Reports:**  
  - Automated periodic reports generated from historical and real-time data.
- **User-Defined Alerts:**  
  - Customizable alerts for key performance indicators (KPIs) integrated into the BI dashboards.

This detailed BI model documentation ensures that SkyOptima provides actionable insights, facilitating data-driven decision-making and continuous improvement.
