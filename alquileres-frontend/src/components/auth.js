import React, { useState } from 'react';
import Register from './Register';
import Login from './Login';

const Auth = () => {
  const [activeForm, setActiveForm] = useState(null);

  const handleRegisterClick = () => {
    setActiveForm(activeForm === 'register' ? null : 'register');
  };

  const handleLoginClick = () => {
    setActiveForm(activeForm === 'login' ? null : 'login');
  };

  return (
    <div className="auth-container">
      <button
        className={`auth-glass-btn ${activeForm === 'register' ? 'active' : ''}`}
        onClick={handleRegisterClick}
        aria-pressed={activeForm === 'register'}
      >
        <span role="img" aria-label="register">📝</span>
        {activeForm === 'register' ? 'Cerrar Registro' : 'Registro'}
      </button>
      <button
        className={`auth-glass-btn ${activeForm === 'login' ? 'active' : ''}`}
        onClick={handleLoginClick}
        aria-pressed={activeForm === 'login'}
      >
        <span role="img" aria-label="login">🔑</span>
        {activeForm === 'login' ? 'Cerrar Login' : 'Login'}
      </button>
      <div className="auth-form-area">
        {activeForm === 'register' && <Register />}
        {activeForm === 'login' && <Login />}
      </div>
    </div>
  );
};

export default Auth;