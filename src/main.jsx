import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './QuantumNexusDashboard.jsx' // هنا خلينا الـ App يستدعي ملف الكوانتم بتاعك مباشرة

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)
