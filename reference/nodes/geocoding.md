# geocoding — usage and limitations

Evidence: observed configuration unless otherwise dated below; not a guarantee of execution or exhaustive options. Historical resource IDs are examples only. Current project rules override legacy checkpoints/styling.

<a id="geocoding"></a>

### Geocoding — `geocoding`

Maps City as an input with type `city` and requests Country Code with type `country_code`. The source already contains latitude/longitude; this example alone does not establish how those values are handled.

- **Property class:** `DataFlowNodeGeocodingProperties:#Infinis.DataFlows`.
- **Observed upstream source counts:** 1.
- **Node-specific properties:** `GeocodeInputColumns`, `GeocodeOutputColumns`.
- **Fixture examples:** `Geocoding #1`.

Observed node-specific settings (not a complete node):

```json
{
  "GeocodeInputColumns": [
    {
      "Column": "City",
      "Type": "city"
    }
  ],
  "GeocodeOutputColumns": [
    {
      "Column": "Country Code",
      "Type": "country_code"
    }
  ]
}
```
