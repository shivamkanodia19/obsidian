import fs from "node:fs/promises";
import path from "node:path";
import { SpreadsheetFile, Workbook } from "@oai/artifact-tool";

const ROOT = "C:/Users/shiva/obsidian";
const OUT_DIR = path.join(ROOT, "05_Outputs", "research-analysis", "legends-merch-assessment-2026-05-07");
const ARTIFACTS_DIR = path.join(OUT_DIR, "artifacts");
const OUTPUT_XLSX = path.join(OUT_DIR, "Legends_Merch_Sales_Assessment.xlsx");

function readCsv(file) {
  return fs.readFile(path.join(ARTIFACTS_DIR, file), "utf8");
}

function csvToRows(text) {
  const lines = text.trim().split(/\r?\n/);
  const rows = [];
  for (const line of lines) {
    const row = [];
    let current = "";
    let inQuotes = false;
    for (let i = 0; i < line.length; i += 1) {
      const ch = line[i];
      if (ch === '"') {
        if (inQuotes && line[i + 1] === '"') {
          current += '"';
          i += 1;
        } else {
          inQuotes = !inQuotes;
        }
      } else if (ch === "," && !inQuotes) {
        row.push(current);
        current = "";
      } else {
        current += ch;
      }
    }
    row.push(current);
    rows.push(
      row.map((value) => {
        if (value === "") return "";
        const asNum = Number(value);
        return Number.isFinite(asNum) && /^-?\d+(\.\d+)?$/.test(value) ? asNum : value;
      }),
    );
  }
  return rows;
}

function num(value, digits = 0) {
  return Number(value.toFixed(digits));
}

function pct(value, digits = 1) {
  return `${(value * 100).toFixed(digits)}%`;
}

function money(value) {
  return Number(value.toFixed(2));
}

function fmtCurrency(value) {
  return new Intl.NumberFormat("en-US", {
    style: "currency",
    currency: "USD",
    maximumFractionDigits: 2,
  }).format(value);
}

function fmtInteger(value) {
  return new Intl.NumberFormat("en-US", {
    maximumFractionDigits: 0,
  }).format(value);
}

function applyTitleBand(range) {
  range.format = {
    fill: "#143642",
    font: { color: "#FFFFFF", bold: true, size: 16 },
    horizontalAlignment: "center",
    verticalAlignment: "center",
  };
}

function applySectionBand(range) {
  range.format = {
    fill: "#EDE6D6",
    font: { color: "#143642", bold: true, size: 11 },
    horizontalAlignment: "left",
    verticalAlignment: "center",
  };
}

function applyHeader(range) {
  range.format = {
    fill: "#2D6A4F",
    font: { color: "#FFFFFF", bold: true, size: 10 },
    horizontalAlignment: "center",
    verticalAlignment: "center",
    wrapText: true,
  };
}

function styleDataBody(range) {
  range.format = {
    font: { color: "#1F2937", size: 10 },
    verticalAlignment: "center",
  };
}

async function main() {
  const workbook = Workbook.create();
  const dashboard = workbook.worksheets.add("Dashboard");
  const categorySheet = workbook.worksheets.add("Category YoY");
  const zoneSheet = workbook.worksheets.add("Zone YoY");
  const monthlySheet = workbook.worksheets.add("Monthly Trend");
  const zoneCategorySheet = workbook.worksheets.add("Zone-Category");
  const notesSheet = workbook.worksheets.add("Data Notes");

  dashboard.showGridLines = false;
  categorySheet.showGridLines = false;
  zoneSheet.showGridLines = false;
  monthlySheet.showGridLines = false;
  zoneCategorySheet.showGridLines = false;
  notesSheet.showGridLines = false;

  const [overallRows, categoryRows, zoneRows, monthlyRows, zoneCategoryRows] = await Promise.all([
    readCsv("overall_metrics.csv"),
    readCsv("category_yoy.csv"),
    readCsv("zone_yoy.csv"),
    readCsv("monthly_revenue.csv"),
    readCsv("zone_category_growth.csv"),
  ]);

  const quality = JSON.parse(await fs.readFile(path.join(ARTIFACTS_DIR, "data_quality.json"), "utf8"));
  const categoryData = csvToRows(categoryRows);
  const zoneData = csvToRows(zoneRows);
  const monthlyData = csvToRows(monthlyRows);
  const zoneCategoryData = csvToRows(zoneCategoryRows);
  const overallData = csvToRows(overallRows);

  categorySheet.getRange(`A1:N${categoryData.length}`).values = categoryData;
  zoneSheet.getRange(`A1:N${zoneData.length}`).values = zoneData;
  monthlySheet.getRange(`A1:D${monthlyData.length}`).values = monthlyData;
  zoneCategorySheet.getRange(`A1:F${zoneCategoryData.length}`).values = zoneCategoryData;
  notesSheet.getRange("A1:B10").values = [
    ["Data Note", "Explanation"],
    ["Source file", "mlb_retail_sales_2yr.csv"],
    ["Rows in raw file", quality.raw_row_count],
    ["Rows used in analysis", quality.clean_row_count],
    ["Rows excluded", quality.excluded_rows],
    ["Season scope", "2023 and 2024 only"],
    ["Season anomaly", "276 malformed rows were labeled 2022 but used 2023 game IDs; excluded from YoY."],
    ["Category cleanup", "Trimmed whitespace and standardized Jersy to Jersey."],
    ["Location field used", "store_zone"],
    ["Location caveat", "store_id was not stable across zones, so zone-level location analysis is the reliable comparison."],
  ];

  categorySheet.getRange("A1:N1").format.rowHeightPx = 28;
  zoneSheet.getRange("A1:N1").format.rowHeightPx = 28;
  monthlySheet.getRange("A1:D1").format.rowHeightPx = 28;
  zoneCategorySheet.getRange("A1:F1").format.rowHeightPx = 28;
  notesSheet.getRange("A1:B1").format.rowHeightPx = 28;

  applyHeader(categorySheet.getRange("A1:N1"));
  applyHeader(zoneSheet.getRange("A1:N1"));
  applyHeader(monthlySheet.getRange("A1:D1"));
  applyHeader(zoneCategorySheet.getRange("A1:F1"));
  applyHeader(notesSheet.getRange("A1:B1"));

  styleDataBody(categorySheet.getRange(`A2:N${categoryData.length}`));
  styleDataBody(zoneSheet.getRange(`A2:N${zoneData.length}`));
  styleDataBody(monthlySheet.getRange(`A2:D${monthlyData.length}`));
  styleDataBody(zoneCategorySheet.getRange(`A2:F${zoneCategoryData.length}`));
  styleDataBody(notesSheet.getRange("A2:B10"));

  categorySheet.freezePanes.freezeRows(1);
  zoneSheet.freezePanes.freezeRows(1);
  monthlySheet.freezePanes.freezeRows(1);
  zoneCategorySheet.freezePanes.freezeRows(1);
  notesSheet.freezePanes.freezeRows(1);

  categorySheet.getRange("B2:C100").format.numberFormat = "$#,##0.00";
  categorySheet.getRange("D2:G100").format.numberFormat = "0";
  categorySheet.getRange("H2:H100").format.numberFormat = "$#,##0.00";
  categorySheet.getRange("I2:K100").format.numberFormat = "0.0%";
  categorySheet.getRange("L2:M100").format.numberFormat = "$#,##0.00";
  categorySheet.getRange("N2:N100").format.numberFormat = "0.0%";
  zoneSheet.getRange("B2:C100").format.numberFormat = "$#,##0.00";
  zoneSheet.getRange("D2:G100").format.numberFormat = "0";
  zoneSheet.getRange("H2:H100").format.numberFormat = "$#,##0.00";
  zoneSheet.getRange("I2:K100").format.numberFormat = "0.0%";
  zoneSheet.getRange("L2:M100").format.numberFormat = "$#,##0.00";
  zoneSheet.getRange("N2:N100").format.numberFormat = "0.0%";
  monthlySheet.getRange("C2:C20").format.numberFormat = "$#,##0.00";
  monthlySheet.getRange("D2:D20").format.numberFormat = "0";
  zoneCategorySheet.getRange("C2:F100").format.numberFormat = "$#,##0.00";
  zoneCategorySheet.getRange("F2:F100").format.numberFormat = "0.0%";

  categorySheet.getRange("A1:N100").format.autofitColumns();
  zoneSheet.getRange("A1:N100").format.autofitColumns();
  monthlySheet.getRange("A1:D20").format.autofitColumns();
  zoneCategorySheet.getRange("A1:F100").format.autofitColumns();
  notesSheet.getRange("A1:B10").format.autofitColumns();

  const season2023 = overallData.find((row) => row[0] === 2023);
  const season2024 = overallData.find((row) => row[0] === 2024);
  const revenueGrowthPct = season2024[1] / season2023[1] - 1;
  const txnGrowthPct = season2024[2] / season2023[2] - 1;
  const unitGrowthPct = season2024[3] / season2023[3] - 1;
  const basketGrowthPct = season2024[11] / season2023[11] - 1;

  dashboard.getRange("A1:N2").merge();
  dashboard.getRange("A1").values = [[
    "Legends Merchandise Sales Assessment | 2024 vs. 2023 In-Stadium Retail Performance",
  ]];
  applyTitleBand(dashboard.getRange("A1:N2"));

  dashboard.getRange("A4:N5").merge();
  dashboard.getRange("A4").values = [[
    "Executive Summary: Revenue grew modestly (+0.5%) on the same 81 home games, driven by stronger T-shirt and Jersey demand plus Lower Concourse traffic. The core opportunity is to raise basket size again while fixing zone-level softness in Club Level, Outfield, and Upper Deck.",
  ]];
  dashboard.getRange("A4:N5").format = {
    fill: "#FAFAF7",
    font: { color: "#143642", size: 11 },
    wrapText: true,
    verticalAlignment: "center",
  };

  dashboard.getRange("A7:N7").merge();
  dashboard.getRange("A7").values = [["Core KPIs"]];
  applySectionBand(dashboard.getRange("A7:N7"));

  const kpis = [
    ["Revenue", fmtCurrency(season2024[1]), pct(revenueGrowthPct)],
    ["Transactions", fmtInteger(season2024[2]), pct(txnGrowthPct)],
    ["Units Sold", fmtInteger(season2024[3]), pct(unitGrowthPct)],
    ["Sales / Transaction", fmtCurrency(season2024[11]), pct(basketGrowthPct)],
  ];

  const starts = ["A9:C12", "D9:F12", "G9:I12", "J9:L12"];
  for (let i = 0; i < kpis.length; i += 1) {
    const [label, value, change] = kpis[i];
    const range = dashboard.getRange(starts[i]);
    range.merge();
    range.values = [[`${label}\n2024: ${value}\nYoY: ${change}`]];
    range.format = {
      fill: "#EDE6D6",
      font: { color: "#143642", bold: true, size: 11 },
      horizontalAlignment: "center",
      verticalAlignment: "center",
      wrapText: true,
    };
  }

  dashboard.getRange("A14:N14").merge();
  dashboard.getRange("A14").values = [["SWOT"]];
  applySectionBand(dashboard.getRange("A14:N14"));

  const swotBlocks = {
    Strengths: [
      "Revenue grew 0.5% on flat schedule volume (81 games each season).",
      "T-shirts led category growth and Jerseys remained the anchor at 37.8% of 2024 revenue.",
      "Lower Concourse added $21.8K and captured the biggest share gain.",
    ],
    Weaknesses: [
      "Sales per transaction fell 0.7%, so conversion improved faster than basket size.",
      "Three of five stadium zones declined YoY.",
      "Caps and Hoodies softened despite major revenue share.",
    ],
    Opportunities: [
      "Expand jersey and T-shirt space in Lower/Main Concourse.",
      "Run July-August bundle and add-on programs to reverse the midseason dip.",
      "Use zone-specific assortment resets where premium items underperformed.",
    ],
    Threats: [
      "Revenue concentration remains high in Jerseys and Hoodies.",
      "Flat overall growth may undershoot the ROI expected from retail upgrades.",
      "Inconsistent master data can slow operational decisions if not fixed.",
    ],
  };
  const swotPositions = [
    ["A16:C21", "Strengths"],
    ["D16:F21", "Weaknesses"],
    ["G16:I21", "Opportunities"],
    ["J16:L21", "Threats"],
  ];
  for (const [cellRange, title] of swotPositions) {
    const block = dashboard.getRange(cellRange);
    block.merge();
    const body = swotBlocks[title].map((line) => `- ${line}`).join("\n");
    block.values = [[`${title}\n${body}`]];
    block.format = {
      fill: "#FAFAF7",
      font: { color: "#1F2937", size: 10, bold: title === "Strengths" || title === "Opportunities" },
      verticalAlignment: "top",
      wrapText: true,
    };
  }

  dashboard.getRange("M16:N21").merge();
  dashboard.getRange("M16").values = [[
    "Data prep notes\n- Excluded 276 malformed 2022 rows\n- Standardized Jersy/Jersey and Keychain whitespace\n- Used store_zone instead of store_id for location analysis",
  ]];
  dashboard.getRange("M16:N21").format = {
    fill: "#F4F1EA",
    font: { color: "#1F2937", size: 9 },
    verticalAlignment: "top",
    wrapText: true,
  };

  dashboard.getRange("A23:N23").merge();
  dashboard.getRange("A23").values = [["Charts"]];
  applySectionBand(dashboard.getRange("A23:N23"));

  monthlySheet.getRange("F1:H8").values = [
    ["Month", "2023 Revenue", "2024 Revenue"],
    ...["Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct"].map((month) => {
      const row2023 = monthlyData.find((row) => row[0] === 2023 && row[1] === month);
      const row2024 = monthlyData.find((row) => row[0] === 2024 && row[1] === month);
      return [month, row2023?.[2] ?? 0, row2024?.[2] ?? 0];
    }),
  ];
  applyHeader(monthlySheet.getRange("F1:H1"));
  styleDataBody(monthlySheet.getRange("F2:H8"));
  monthlySheet.getRange("G2:H8").format.numberFormat = "$#,##0.00";
  monthlySheet.getRange("F1:H8").format.autofitColumns();

  categorySheet.getRange("P1:R8").values = [
    ["Category", "2023 Revenue", "2024 Revenue"],
    ...categoryData.slice(1).map((row) => [row[0], row[1], row[2]]),
  ];
  applyHeader(categorySheet.getRange("P1:R1"));
  styleDataBody(categorySheet.getRange("P2:R8"));
  categorySheet.getRange("Q2:R8").format.numberFormat = "$#,##0.00";
  categorySheet.getRange("P1:R8").format.autofitColumns();

  zoneSheet.getRange("P1:Q6").values = [
    ["Zone", "Growth $"],
    ...zoneData.slice(1).map((row) => [row[0], row[7]]),
  ];
  applyHeader(zoneSheet.getRange("P1:Q1"));
  styleDataBody(zoneSheet.getRange("P2:Q6"));
  zoneSheet.getRange("Q2:Q6").format.numberFormat = "$#,##0.00";
  zoneSheet.getRange("P1:Q6").format.autofitColumns();

  const heatRows = zoneCategoryData.slice(1);
  const zones = [...new Set(heatRows.map((row) => row[0]))];
  const items = [...new Set(heatRows.map((row) => row[1]))];
  const heatMatrix = [["Zone", ...items]];
  for (const zoneName of zones) {
    const row = [zoneName];
    for (const item of items) {
      const match = heatRows.find((entry) => entry[0] === zoneName && entry[1] === item);
      row.push(match?.[4] ?? 0);
    }
    heatMatrix.push(row);
  }
  dashboard.getRange("G39:N44").values = heatMatrix;
  applyHeader(dashboard.getRange("G39:N39"));
  styleDataBody(dashboard.getRange("G40:N44"));
  dashboard.getRange("H40:N44").format.numberFormat = "$#,##0.00";
  dashboard.getRange("H40:N44").conditionalFormats.addColorScale({
    minColor: "#B23A48",
    midColor: "#FFF8E8",
    maxColor: "#2D6A4F",
  });

  const lineChart = dashboard.charts.add("line", monthlySheet.getRange("F1:H8"));
  lineChart.setPosition("A25", "F37");
  lineChart.title = "Monthly Revenue Trend";
  lineChart.hasLegend = true;
  lineChart.xAxis = { axisType: "textAxis" };
  lineChart.yAxis = { numberFormatCode: "$#,##0" };

  const categoryChart = dashboard.charts.add("bar", categorySheet.getRange("P1:R8"));
  categoryChart.setPosition("H25", "N37");
  categoryChart.title = "Category Revenue";
  categoryChart.hasLegend = true;
  categoryChart.xAxis = { axisType: "textAxis" };
  categoryChart.yAxis = { numberFormatCode: "$#,##0" };

  const zoneChart = dashboard.charts.add("bar", zoneSheet.getRange("P1:Q6"));
  zoneChart.setPosition("A39", "F52");
  zoneChart.title = "Zone Growth Contribution";
  zoneChart.hasLegend = false;
  zoneChart.xAxis = { axisType: "textAxis" };
  zoneChart.yAxis = { numberFormatCode: "$#,##0" };

  dashboard.getRange("G46:N46").merge();
  dashboard.getRange("G46").values = [[
    "Heatmap highlight: Lower Concourse Jerseys drove the biggest gain (+$24.4K), while Outfield Jerseys were the largest drag (-$8.8K).",
  ]];
  dashboard.getRange("G46:N46").format = {
    fill: "#FAFAF7",
    font: { color: "#1F2937", size: 10 },
    wrapText: true,
    verticalAlignment: "top",
  };

  dashboard.getRange("G48:N53").merge();
  dashboard.getRange("G48").values = [[
    "Recommendations\n1. Expand jersey and T-shirt adjacencies in Lower and Main Concourse.\n2. Use bundles and add-on signage to recover basket size in July and August.\n3. Reset Club, Outfield, and Upper Deck assortments around local demand rather than uniform category allocation.\n4. Clean item and location master data before next season so store-level testing is measurable.",
  ]];
  dashboard.getRange("G48:N53").format = {
    fill: "#F4F1EA",
    font: { color: "#1F2937", size: 10 },
    wrapText: true,
    verticalAlignment: "top",
  };

  const dashboardWidths = [95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 110, 110];
  for (let i = 0; i < dashboardWidths.length; i += 1) {
    dashboard.getCell(0, i).format.columnWidthPx = dashboardWidths[i];
  }

  dashboard.getRange("A1:N2").format.rowHeightPx = 26;
  dashboard.getRange("A4:N5").format.rowHeightPx = 24;
  dashboard.getRange("A7:N7").format.rowHeightPx = 20;
  dashboard.getRange("A9:N12").format.rowHeightPx = 26;
  dashboard.getRange("A14:N14").format.rowHeightPx = 20;
  dashboard.getRange("A16:N21").format.rowHeightPx = 22;
  dashboard.getRange("A23:N23").format.rowHeightPx = 20;
  dashboard.getRange("A39:N44").format.rowHeightPx = 22;
  dashboard.getRange("A46:N46").format.rowHeightPx = 28;
  dashboard.getRange("A48:N53").format.rowHeightPx = 22;

  dashboard.freezePanes.freezeRows(7);

  const check = await workbook.inspect({
    kind: "table",
    range: "Dashboard!A1:N30",
    include: "values",
    tableMaxRows: 30,
    tableMaxCols: 14,
  });
  console.log(check.ndjson);

  const errorScan = await workbook.inspect({
    kind: "match",
    searchTerm: "#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A",
    options: { useRegex: true, maxResults: 100 },
    summary: "formula error scan",
  });
  console.log(errorScan.ndjson);

  await fs.mkdir(OUT_DIR, { recursive: true });
  const xlsx = await SpreadsheetFile.exportXlsx(workbook);
  await xlsx.save(OUTPUT_XLSX);
  console.log(`Saved workbook to ${OUTPUT_XLSX}`);
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
