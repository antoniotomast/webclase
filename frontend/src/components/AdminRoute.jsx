import { Navigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';

const AdminRoute = ({ children }) => {
  const { user, loading } = useAuth();

  if (loading) {
    return <div className="loading">Cargando...</div>;
  }

  if (!user) {
    return <Navigate to="/login" replace />;
  }

  if (user.role !== 'admin') {
    return (
      <div className="error-page">
        <h1>403</h1>
        <h2>Acceso Prohibido</h2>
        <p>No tienes permisos para acceder a esta página.</p>
        <p>Se requiere rol de administrador.</p>
        <a href="/" className="btn btn-primary">Volver al inicio</a>
      </div>
    );
  }

  return children;
};

export default AdminRoute;
