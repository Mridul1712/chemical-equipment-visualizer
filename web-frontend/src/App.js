import React, { useState } from "react";
import axios from "axios";

import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
} from "chart.js";

import { Bar } from "react-chartjs-2";

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
);

function App() {
  const [summary, setSummary] = useState(null);
  const [error, setError] = useState("");

  const uploadCSV = async (e) => {
    const file = e.target.files[0];
    if (!file) return;

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/api/upload/",
        formData
      );
      setSummary(response.data);
      setError("");
    } catch (err) {
      setError("Upload failed. Is backend running?");
    }
  };

  const chartData = summary
    ? {
        labels: Object.keys(summary.type_distribution),
        datasets: [
          {
            label: "Equipment Count",
            data: Object.values(summary.type_distribution),
            backgroundColor: "rgba(54, 162, 235, 0.6)",
          },
        ],
      }
    : null;

  return (
    <div style={{ padding: "20px", fontFamily: "Arial" }}>
      <h1>Chemical Equipment Parameter Visualizer</h1>

      <input type="file" accept=".csv" onChange={uploadCSV} />

      {error && <p style={{ color: "red" }}>{error}</p>}

      {summary && (
        <div style={{ marginTop: "20px" }}>
          <h2>Summary</h2>
          <p>Total Equipment: {summary.total_equipment}</p>
          <p>Average Flowrate: {summary.avg_flowrate}</p>
          <p>Average Pressure: {summary.avg_pressure}</p>
          <p>Average Temperature: {summary.avg_temperature}</p>

          <h2>Equipment Type Distribution</h2>
          <Bar data={chartData} />
        </div>
      )}
    </div>
  );
}

export default App;
