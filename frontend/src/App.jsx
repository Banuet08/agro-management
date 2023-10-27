import React, { useState } from 'react';
import axios from 'axios';

function LoginForm({ history }) {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await axios.post('http://localhost:8000/authentication/login/', {
        username,
        password,
      });

      // Almacenar el token JWT en una cookie (usa una biblioteca como js-cookie o react-cookie)
      // Ejemplo con js-cookie:
      document.cookie = `jwt=${response.data.access_token}; path=/`;
      console.log(response.data)

      // Redirigir a la página de inicio
    
    
    } catch (error) {
      console.error('Error al iniciar sesión:', error);
    }
  };

  return (
    <div>
      <h2>Iniciar Sesión</h2>
      <form onSubmit={handleSubmit}>
        <label>Nombre de usuario:</label>
        <input
          type="text"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />
        <label>Contraseña:</label>
        <input
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        <button type="submit">Iniciar Sesión</button>
      </form>
    </div>
  );
}

export default LoginForm;
