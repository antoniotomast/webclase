import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import api from '../services/api';
import { useAuth } from '../context/AuthContext';

const Actores = () => {
  const [actores, setActores] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const { user } = useAuth();
  const isAdmin = user?.username === 'admin';

  useEffect(() => {
    fetchActores();
  }, []);

  const fetchActores = async () => {
    try {
      const response = await api.get('/actores');
      setActores(response.data);
    } catch (err) {
      setError('Error al cargar los actores');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return <div className="loading">Cargando actores...</div>;
  }

  return (
    <div className="container">
      <div className="table-container">
        <div className="table-header">
          <h2>Lista de Actores 🎭</h2>
        </div>

        {error && <div className="error-message">{error}</div>}

        {actores.length === 0 ? (
          <div className="empty-state">
            <p>No hay actores registrados</p>
          </div>
        ) : (
          <table>
            <thead>
              <tr>
                <th>ID</th>
                <th>Nombre</th>
                {isAdmin && <th>Acciones</th>}
              </tr>
            </thead>
            <tbody>
              {actores.map((actor) => (
                <tr key={actor.id}>
                  <td>{actor.id}</td>
                  <td>{actor.nombre}</td>
                  {isAdmin && (
                    <td>
                      <Link to={`/editar/${actor.id}`} className="btn btn-small btn-primary">
                        Editar
                      </Link>
                    </td>
                  )}
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </div>
    </div>
  );
};

export default Actores;
