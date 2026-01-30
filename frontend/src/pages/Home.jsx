import { useAuth } from '../context/AuthContext';

const Home = () => {
  const { user } = useAuth();

  return (
    <div className="container">
      <div className="table-container">
        <h1>Bienvenido, {user?.username}! 🎬</h1>
        <p style={{ marginTop: '1rem', color: '#7f8c8d' }}>
          Sistema de gestión de actores
        </p>
        
        <div style={{ marginTop: '2rem' }}>
          {user?.username === 'admin' ? (
            <div>
              <h3>Panel de Administración</h3>
              <p>Como administrador puedes:</p>
              <ul style={{ marginTop: '1rem', lineHeight: '2' }}>
                <li>✅ Ver la lista de actores</li>
                <li>✅ Añadir nuevos actores</li>
                <li>✅ Actualizar información de actores</li>
                <li>✅ Eliminar actores</li>
              </ul>
            </div>
          ) : (
            <div>
              <h3>Panel de Usuario</h3>
              <p>Como usuario registrado puedes:</p>
              <ul style={{ marginTop: '1rem', lineHeight: '2' }}>
                <li>✅ Ver la lista de actores</li>
                <li>❌ No puedes añadir, actualizar ni eliminar</li>
              </ul>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default Home;
