import { useState, useEffect } from 'react';
import { useNavigate, useParams, Link } from 'react-router-dom';
import api from '../services/api';

const EditarActor = () => {
  const { id } = useParams();
  const [nombre, setNombre] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(true);
  const [submitting, setSubmitting] = useState(false);
  const navigate = useNavigate();

  useEffect(() => {
    cargarActor();
  }, [id]);

  const cargarActor = async () => {
    try {
      const response = await api.get(`/actores/${id}`);
      setNombre(response.data.nombre);
    } catch (err) {
      setError('Error al cargar el actor');
    } finally {
      setLoading(false);
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');

    if (!nombre.trim()) {
      setError('El nombre es obligatorio');
      return;
    }

    setSubmitting(true);

    try {
      await api.put(`/actores/${id}`, { nombre });
      navigate('/actores');
    } catch (err) {
      setError(err.response?.data?.detail || 'Error al actualizar el actor');
    } finally {
      setSubmitting(false);
    }
  };

  if (loading) {
    return <div className="loading">Cargando actor...</div>;
  }

  return (
    <div className="form-container">
      <h2>Editar Actor</h2>
      
      {error && <div className="error-message">{error}</div>}
      
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="nombre">Nombre del Actor *</label>
          <input
            type="text"
            id="nombre"
            value={nombre}
            onChange={(e) => setNombre(e.target.value)}
            required
            autoFocus
          />
        </div>
        
        <div className="form-actions">
          <button type="submit" className="btn btn-primary" disabled={submitting}>
            {submitting ? 'Actualizando...' : 'Actualizar Actor'}
          </button>
          <Link to="/actores" className="btn btn-secondary">
            Cancelar
          </Link>
        </div>
      </form>
    </div>
  );
};

export default EditarActor;
