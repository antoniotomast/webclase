import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import api from '../services/api';

const BorrarActor = () => {
  const [actores, setActores] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [deleting, setDeleting] = useState(null);
  const navigate = useNavigate();

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

  const handleDelete = async (id, nombre) => {
    if (!window.confirm(`¿Estás seguro de que quieres eliminar a ${nombre}?`)) {
      return;
    }

    setDeleting(id);
    setError('');

    try {
      await api.delete(`/actores/${id}`);
      setActores(actores.filter(actor => actor.id !== id));
    } catch (err) {
      setError(err.response?.data?.detail || 'Error al eliminar el actor');
    } finally {
      setDeleting(null);
    }
  };

  if (loading) {
    return <div className="loading">Cargando actores...</div>;
  }

  return (
    <div className="container">
      <div className="table-container">
        <div className="table-header">
          <h2>Eliminar Actores 🗑️</h2>
          <button className="btn btn-secondary" onClick={() => navigate('/actores')}>
            Volver
          </button>
        </div>

        {error && <div className="error-message">{error}</div>}

        {actores.length === 0 ? (
          <div className="empty-state">
            <p>No hay actores para eliminar</p>
          </div>
        ) : (
          <table>
            <thead>
              <tr>
                <th>ID</th>
                <th>Nombre</th>
                <th>Acciones</th>
              </tr>
            </thead>
            <tbody>
              {actores.map((actor) => (
                <tr key={actor.id}>
                  <td>{actor.id}</td>
                  <td>{actor.nombre}</td>
                  <td>
                    <button
                      className="btn btn-danger btn-sm"
                      onClick={() => handleDelete(actor.id, actor.nombre)}
                      disabled={deleting === actor.id}
                    >
                      {deleting === actor.id ? 'Eliminando...' : 'Eliminar'}
                    </button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </div>
    </div>
  );
};

export default BorrarActor;
