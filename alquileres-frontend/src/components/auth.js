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
    <div>
      <button
        className="auth-button"
        onClick={handleRegisterClick}
        aria-pressed={activeForm === 'register'}
      >
        {activeForm === 'register' ? 'Cerrar Registro' : 'Registro'}
      </button>
      <button
        className="auth-button"
        onClick={handleLoginClick}
        aria-pressed={activeForm === 'login'}
      >
        {activeForm === 'login' ? 'Cerrar Login' : 'Login'}
      </button>
      {activeForm === 'register' && <Register />}
      {activeForm === 'login' && <Login />}
    </div>
  );
};

export default Auth;