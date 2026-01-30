import { Link } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';

const Navbar = () => {
  const { user, logout } = useAuth();

  const handleLogout = async () => {
    try {
      await logout();
    } catch (error) {
      console.error('Error al cerrar sesión:', error);
    }
  };

  if (!user) {
    return null;
  }

  return (
    <nav className="navbar">
      <div className="navbar-content">
        <h1>Sistema de Gestión de Actores 🎬</h1>
        <div className="navbar-menu">
          <Link to="/">Inicio</Link>
          <Link to="/actores">Ver Actores</Link>
          {user.username === 'admin' && (
            <>
              <Link to="/insertar">Insertar Actor</Link>
              <Link to="/borrar">Borrar Actor</Link>
            </>
          )}
        </div>
        <div className="navbar-user">
          <div className="user-info">
            <span>👤 {user.username}</span>
            {user.username === 'admin' && (
              <span className="user-badge">ADMIN</span>
            )}
          </div>
          <button onClick={handleLogout} className="btn btn-danger btn-sm">
            Cerrar Sesión
          </button>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
