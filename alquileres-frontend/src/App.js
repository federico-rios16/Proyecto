import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Welcome from './components/Welcome';
import Student from './components/Student';
import Register from './components/Register';
import Login from './components/Login';
import Dashboard from './components/Dashboard';
import Support from './components/Support';
import Wallet from './components/Wallet';
import Navigation from './components/Navbar';
import Auth from './components/auth'; // Importa el componente Auth

function App() {
  return (
    <Router>
      <Navigation />
      <Routes>
        <Route path="/" element={<Welcome />} />
        <Route path="/student" element={<Student />} />
        <Route path="/register" element={<Register />} />
        <Route path="/login" element={<Login />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/support" element={<Support />} />
        <Route path="/wallet" element={<Wallet />} />
        <Route path="/auth" element={<Auth />} /> {/* Nueva ruta para Auth */}
      </Routes>
    </Router>
  );
}

export default App;
