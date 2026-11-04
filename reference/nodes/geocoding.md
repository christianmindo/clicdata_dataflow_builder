# geocoding — usage and limitations

## Output selection and downstream mapping — observed 2026-11-04

A user-returned service-branch export contains GeocodeCountryCode but no GeocodeLatitude/GeocodeLongitude before the IP node. The generated Geocoding configuration selected only country_code; the historical exampleOutputSchema's latitude/longitude fields did not establish automatic coordinate emission. Do not add coordinates to downstream schemas or rename mappings unless they are actually requested using verified settings and present in the current export. The supplied IP node correctly names its independently requested coordinates IPLatitude and IPLongitude (double). Its Table Output had stale GeocodeLatitude/GeocodeLongitude mappings, which must be removed for that observed schema. This is schema evidence, not an execution test or proof of additional geocoding output Type enums.

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
