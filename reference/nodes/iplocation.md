# iplocation — usage and limitations

Evidence: observed configuration unless otherwise dated below; not a guarantee of execution or exhaustive options. Historical resource IDs are examples only. Current project rules override legacy checkpoints/styling.

<a id="iplocation"></a>

### IP to Location — `iplocation`

Uses an IP source column and requests latitude/longitude output fields. Provider, invalid-IP handling, and supported additional outputs are unknown.

- **Property class:** `DataFlowNodeIPToLocationProperties:#Infinis.DataFlows`.
- **Observed upstream source counts:** 1.
- **Node-specific properties:** `ProcessOutputColumns`, `SourceColumn`.
- **Fixture examples:** `IP to Location #1`.

Observed node-specific settings (not a complete node):

```json
{
  "ProcessOutputColumns": [
    {
      "Name": "Latitude",
      "Type": "latitude"
    },
    {
      "Name": "Longitude",
      "Type": "longitude"
    }
  ],
  "SourceColumn": "IP"
}
```


## City / country code and output selector — 2026-10-28

A user-supplied configured export confirms latitude and longitude as double, country_code as textsimple(250), and city as text(250). The export retains all five incoming web-visit fields and appends these four attributes. Country Code is a code, not a full country name; no full-country-name output appears in the supplied selector.

```json
{
  "SourceColumn": "IPAddress",
  "ProcessOutputColumns": [
    {
      "Name": "Latitude",
      "Type": "latitude"
    },
    {
      "Name": "Longitude",
      "Type": "longitude"
    },
    {
      "Name": "Country Code",
      "Type": "country_code"
    },
    {
      "Name": "City",
      "Type": "city"
    }
  ]
}
```

The screenshot additionally lists Continent Code, Region, District, Zip Code, Weather Code, Timezone Code, Timezone Offset and ISP. These are UI labels only; their serialized Type identifiers and schema types remain unverified. The visible property panel has no failure-mode control. Invalid/private/empty IP handling, IPv6 behavior, null outputs and row retention require editor testing. Do not invent OnFailure settings. Info/identity metadata from the export is not a requirement to reproduce personal ownership data.


## Supplemental API enum evidence — 2026-10-28

The official 2026.3 reference documents all 12 IP output Type strings. See [the optional API parameter reference](../api/README.md) only when a requested output is not covered by a clipboard sample. Four are already clipboard-confirmed; the remaining eight are API-documented candidates, not unknown guessed strings. This does not establish their clipboard schema types or IP failure behavior.


## User-reported unavailable-location result — 2026-10-28

After the synthetic web-visits test, the user reported that unavailable IP locations are NULL and described them as skipped. In the context of the requested row-presence check, this supports retaining the tested visits with null enrichment values rather than dropping their rows. Treat this as a user-reported editor result, not an independently captured full preview audit; no exact row-count report or per-IP outcome was supplied. The downstream fallback can replace missing City/Country Code labels with N/A while Latitude/Longitude remain numeric/null. Do not generalize this result to service outages, provider limits or every IP format. Earlier notes that this behavior was entirely untested are superseded for this tested scenario only.
