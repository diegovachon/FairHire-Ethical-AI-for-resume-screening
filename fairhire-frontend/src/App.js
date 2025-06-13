import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);
  
  const handleFileChange = (e) => {
    // It sets the file in state so it can be uploaded
    setFile(e.target.files[0]);
  };

  const handleSubmit = async () => {
    if (!file) return;
    const formData = new FormData();
    formData.append('file', file);

    try {
      const res = await axios.post('http://127.0.0.1:8000/upload_resume', formData);
      setResult(res.data);
    } catch (error) {
      console.error('Upload failed', error);
    }
  };

  const runBiasAudit = async () => {
    try {
      const res = await axios.get('http://127.0.0.1:8000/bias_audit');
      alert(JSON.stringify(res.data, null, 2));
    } catch (error) {
      console.error('Bias audit failed', error);
    }
  };
  <button onClick={runBiasAudit}>Run Bias Audit</button>

  return (
    <div style={{ padding: 20 }}>
      <h1>FairHire Resume Screening</h1>
      <input type="file" accept=".txt" onChange={handleFileChange} />
      <button onClick={handleSubmit}>Upload Resume</button>

      {result && (
        <div style={{ marginTop: 20 }}>
          <h2>Results</h2>
          <p><strong>Score:</strong> {result.score}</p>
          <p><strong>PII Found:</strong></p>
          <pre>{JSON.stringify(result.pii_found, null, 2)}</pre>
          <p><strong>Explanation:</strong></p>
          <ul>
            {result.explanation.map((item, index) => (
              <li key={index}>{item}</li>
            ))}
          </ul>
          <p><strong>Redacted Resume:</strong></p>
          <pre>{result.redacted}</pre>
        </div>
      )}
    </div>
  );
}

export default App;