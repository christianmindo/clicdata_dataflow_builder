# column-selector — usage and limitations

Evidence: observed configuration unless otherwise dated below; not a guarantee of execution or exhaustive options. Historical resource IDs are examples only. Current project rules override legacy checkpoints/styling.

<a id="column-selector"></a>

### Column Selector — `column-selector`

Configures excluded, renamed, and ordered columns. The original QA examples have empty rename/sort arrays. Later retailer exports establish `RenamedColumns` entries with `Name` (source) and `Alias` (output), and `SortedColumnNames` as an array of field-name strings. Do not assume whether sorting names are evaluated before or after renaming; the historical export uses source names in that array.

- **Property class:** `DataFlowNodeColumnSelectorProperties:#Infinis.DataFlows`.
- **Observed upstream source counts:** 1.
- **Node-specific properties:** `RenamedColumns`, `SortedColumnNames`, `UnselectedColumnNames`.
- **Fixture examples:** `Column Selector #2 #1`, `Column Selector #2`, `Column Selector #1`.

Observed node-specific settings (not a complete node):

```json
{
  "RenamedColumns": [],
  "SortedColumnNames": [],
  "UnselectedColumnNames": []
}
```

Additional observed retailer configuration (node-specific fragment; source-specific field names):

```json
{
  "RenamedColumns": [
    {
      "Alias": "ITEM DESC",
      "Name": "Item Description"
    },
    {
      "Alias": "ITEM SIZE",
      "Name": "Size"
    },
    {
      "Alias": "ITEM CATEGORY",
      "Name": "Category"
    },
    {
      "Alias": "ITEM SUBCATEGORY EXTERNAL",
      "Name": "External Catalog Sub-Category"
    },
    {
      "Alias": "ITEM SUBSCATEGORY INTERNAL",
      "Name": "Example Brand Sub-Category"
    },
    {
      "Alias": "ITEM FRANCHISE",
      "Name": "Franchise"
    },
    {
      "Alias": "ITEM FAMILY",
      "Name": "Family"
    },
    {
      "Alias": "ITEM STANDARD WHOLESALE COST USD",
      "Name": "Standard Wholesale Cost USD"
    },
    {
      "Alias": "ITEM FORMULA",
      "Name": "Item Formula"
    },
    {
      "Alias": "SIZE GROUP",
      "Name": "Size Group"
    },
    {
      "Alias": "CORE/ENGINE SKU",
      "Name": "Core/Engine SKU"
    },
    {
      "Alias": "ACTIVE",
      "Name": "Inactive/Historical SKU Flag"
    },
    {
      "Alias": "UPC (INTERNAL)",
      "Name": "UPC"
    },
    {
      "Alias": "SUB-CATEGORY",
      "Name": "Sub-Category"
    }
  ],
  "SortedColumnNames": [
    "Data Load Date/Time",
    "SAP Material ID",
    "UPC",
    "SKU ID",
    "Item Description",
    "Size",
    "Inactive/Historical SKU Flag",
    "Category",
    "External Catalog Sub-Category",
    "Franchise",
    "Family",
    "Item Formula",
    "MSRP USD",
    "Size Group",
    "Core/Engine SKU"
  ],
  "UnselectedColumnNames": [
    "MSRP CAD",
    "MSRP EUR (excluding VAT)",
    "MSRP EUR (including VAT)",
    "MSRP GBP (excluding VAT)",
    "MSRP GBP (including VAT)",
    "Gift Set Flag",
    "TY Retailer A NBT",
    "LY Retailer A NBT",
    "LLY Retailer A NBT",
    "TY Retailer A Tip End Cap Flag",
    "LY Retailer A Tip End Cap Flag",
    "LLY Retailer A Tip End Cap Flag",
    "TY Retailer A Tip 1 Bay",
    "LY Retailer A Tip 1 Bay",
    "LLY Retailer A Tip 1 Bay",
    "TY Retailer B Heritage Upper Section Flag",
    "LY Retailer B Heritage Upper Section Flag",
    "LLY Retailer B Heritage Upper Section Flag",
    "TY Retailer B Heritage Lower Section Flag",
    "LY Retailer B Heritage Lower Section Flag",
    "LLY Retailer B Heritage Lower Section Flag",
    "TY Retailer B Heritage w Supernaturals Upper Section Flag",
    "LY Retailer B Heritage w Supernaturals Upper Section Flag",
    "LLY Retailer B Heritage w Supernaturals Upper Section Flag",
    "TY Retailer B Heritage w Supernaturals Lower Section Flag",
    "LY Retailer B Heritage w Supernaturals Lower Section Flag",
    "LLY Retailer B Heritage w Supernaturals Lower Section Flag",
    "Priority Flag"
  ]
}
```
