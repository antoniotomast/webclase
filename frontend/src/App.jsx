import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { AuthProvider } from './context/AuthContext';
import Navbar from './components/Navbar';
import Login from './pages/Login';
import Register from './pages/Register';
import Home from './pages/Home';
import Actores from './pages/Actores';
import InsertarActor from './pages/InsertarActor';
import EditarActor from './pages/EditarActor';
import BorrarActor from './pages/BorrarActor';
import PrivateRoute from './components/PrivateRoute';
import AdminRoute from './components/AdminRoute';

function App() {
  return (
    <AuthProvider>
      <Router>
        <div className="App">
          <Navbar />
          <Routes>
            {/* Rutas públicas */}
            <Route path="/login" element={<Login />} />
            <Route path="/register" element={<Register />} />
            <Route path="/" element={<Home />} />
            
            {/* Rutas protegidas - requieren autenticación */}
            <Route path="/actores" element={<PrivateRoute><Actores /></PrivateRoute>} />
            
            {/* Rutas de administrador */}
            <Route path="/insertar" element={<AdminRoute><InsertarActor /></AdminRoute>} />
            <Route path="/editar/:id" element={<AdminRoute><EditarActor /></AdminRoute>} />
            <Route path="/borrar" element={<AdminRoute><BorrarActor /></AdminRoute>} />
            
            {/* Ruta por defecto */}
            <Route path="*" element={<Navigate to="/" replace />} />
          </Routes>
        </div>
      </Router>
    </AuthProvider>
  );
}

export default App;
