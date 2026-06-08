import fs from "node:fs/promises";
import path from "node:path";
import { FileBlob, SpreadsheetFile } from "@oai/artifact-tool";
const root = "C:/Users/shiva/obsidian/05_Outputs/research-analysis/legends-merch-assessment-2026-05-07";
const file = await FileBlob.load(path.join(root, "Legends_Merch_Sales_Assessment.xlsx"));
const workbook = await SpreadsheetFile.importXlsx(file);
const blob = await workbook.render({ sheetName: "Dashboard", range: "A1:N56", scale: 2, format: "png", autoCrop: "all" });
await fs.writeFile(path.join(root, "dashboard_preview.png"), new Uint8Array(await blob.arrayBuffer()));
console.log(path.join(root, "dashboard_preview.png"));
