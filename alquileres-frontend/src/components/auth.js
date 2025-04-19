import React, { useState } from 'react';
import Register from './Register';
import Login from './Login';

const Auth = () => {
  const [showRegister, setShowRegister] = useState(false);
  const [showLogin, setShowLogin] = useState(false);

  const handleRegisterClick = () => {
    setShowRegister(true);
  };

  const handleLoginClick = () => {
    setShowLogin(true);
  };

  return (
    <div>
      <button className="auth-button" onClick={handleRegisterClick}>Registro</button>
      <button className="auth-button" onClick={handleLoginClick}>Login</button>
      {showRegister && <Register />}
      {showLogin && <Login />}
    </div>
  );
};

export default Auth;