import React, { useState } from "react";
import axios from "axios";

export default function App() {
  const [file, setFile] = useState(null);
  const [query, setQuery] = useState("Summarise my Blood Test Report");
  const [userId, setUserId] = useState("anonymous_user");
  const [taskId, setTaskId] = useState("");
  const [result, setResult] = useState(null);
  const [status, setStatus] = useState("");

  const handleUpload = async () => {
    if (!file) {
      alert("Please select a PDF file.");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);
    formData.append("query", query);
    formData.append("user_id", userId);

    try {
      const res = await axios.post("http://localhost:8000/analyze", formData);
      setTaskId(res.data.task_id);
      setStatus("processing");
    } catch (err) {
      alert("Upload failed: " + err.message);
    }
  };

  const checkStatus = async () => {
    if (!taskId) return;
    try {
      const res = await axios.get(`http://localhost:8000/status/${taskId}`);
      setStatus(res.data.status);
      if (res.data.result) {
        setResult(res.data.result);
      }
    } catch (err) {
      alert("Status check failed: " + err.message);
    }
  };

  return (
    <div className="p-8 max-w-xl mx-auto text-center">
      <h1 className="text-2xl font-bold mb-4">Blood Test Report Analyser</h1>

      <input
        type="file"
        accept="application/pdf"
        onChange={(e) => setFile(e.target.files[0])}
        className="mb-4"
      />

      <input
        type="text"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Enter query"
        className="mb-4 w-full p-2 border rounded"
      />

      <input
        type="text"
        value={userId}
        onChange={(e) => setUserId(e.target.value)}
        placeholder="Enter User ID"
        className="mb-4 w-full p-2 border rounded"
      />

      <button
        onClick={handleUpload}
        className="bg-blue-600 text-white px-4 py-2 rounded mr-2"
      >
        Upload & Analyze
      </button>

      <button
        onClick={checkStatus}
        className="bg-green-600 text-white px-4 py-2 rounded"
        disabled={!taskId}
      >
        Check Status
      </button>

      {status && <p className="mt-4 font-medium">Status: {status}</p>}

      {result && (
        <div className="mt-4 text-left bg-gray-100 p-4 rounded">
          <h2 className="font-bold mb-2">Analysis Result:</h2>
          <pre className="whitespace-pre-wrap text-sm">{result}</pre>
        </div>
      )}
    </div>
  );
}
