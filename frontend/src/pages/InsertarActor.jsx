import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import api from '../services/api';

const InsertarActor = () => {
  const [nombre, setNombre] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');

    if (!nombre.trim()) {
      setError('El nombre es obligatorio');
      return;
    }

    setLoading(true);

    try {
      await api.post('/actores', { nombre: nombre.trim() });
      navigate('/actores');
    } catch (err) {
      setError(err.response?.data?.detail || 'Error al insertar el actor');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <div className="form-container">
        <h2>Insertar Nuevo Actor 🎬</h2>
        
        {error && <div className="error-message">{error}</div>}
        
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label htmlFor="nombre">Nombre del Actor</label>
            <input
              type="text"
              id="nombre"
              value={nombre}
              onChange={(e) => setNombre(e.target.value)}
              required
              autoFocus
              placeholder="Ej: Leonardo DiCaprio"
            />
          </div>
          
          <div style={{ display: 'flex', gap: '1rem' }}>
            <button type="submit" className="btn btn-success" disabled={loading} style={{ flex: 1 }}>
              {loading ? 'Insertando...' : 'Insertar Actor'}
            </button>
            <button 
              type="button" 
              className="btn btn-secondary" 
              onClick={() => navigate('/actores')}
              style={{ flex: 1 }}
            >
              Cancelar
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default InsertarActor;
