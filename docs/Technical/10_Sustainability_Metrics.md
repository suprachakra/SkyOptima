## Sustainability Metrics
This document details the sustainability metrics and models integrated into SkyOptima to support carbon-aware revenue management.

### Carbon-Aware Pricing Model

SkyOptima incorporates a carbon cost adjustment into fare calculations. The pricing formula includes:
  
$$
P_{fare} = BasePrice + \text{Elasticity} \times (Demand - BaselineDemand) + \lambda_{CO2} \times Emissions_{route}
$$

- **BasePrice:** The baseline fare.
- **Elasticity:** Price sensitivity factor.
- **Demand - BaselineDemand:** Measures excess demand.
- **λ₍CO₂₎:** Real-time EU ETS carbon price (e.g., €98/ton).
- **Emissions₍route₎:** Emission factors for the specific route (tons per passenger).

### Perishables Decay Modeling

For cargo and perishables, the decay model is formulated as:

$$
Q_{fresh} = \int_{t_0}^{t_1} \frac{T_{ambient} - T_{optimal}}{\tau_{decay}} \, dt
$$

- **T₍ambient₎:** Ambient temperature.
- **T₍optimal₎:** Optimal storage temperature.
- **τ₍decay₎:** Decay coefficient (varies by commodity).

### Sustainability KPIs

| KPI                        | Target Value              | Measurement Method                               | Frequency  |
|----------------------------|---------------------------|--------------------------------------------------|------------|
| Carbon Cost per Fare       | Included fully            | API integration with EU ETS pricing             | Daily      |
| Emission Reduction         | 5% reduction target       | Compare forecasted vs actual route emissions      | Monthly    |
| Perishables Load Factor    | ≥97% compliance           | Compare actual vs model-simulated perishables load | Quarterly  |

These metrics are integrated with our continuous monitoring and feedback systems to ensure that every fare calculation reflects both market conditions and environmental impacts.
