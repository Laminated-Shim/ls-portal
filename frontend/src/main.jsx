import React from 'react'
import {
  Route,
  Routes,
  BrowserRouter as Router,
} from "react-router-dom";
import ReactDOM from 'react-dom/client'
import PageNotFound from "./404Page.jsx";
import './index.css'
import AppShell from './AppShell.jsx'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <Router>
      <Routes>
        <Route exact path="/" element={<AppShell />} />
        <Route path="*" element={<PageNotFound />} />
      </Routes>
    </Router>
  </React.StrictMode>,
)
