// Deployment status management
let deploymentInProgress = false;

// Function to show deployment status
function showDeploymentStatus() {
    const statusBox = document.getElementById('deployment-status');
    const timestamp = new Date().toLocaleTimeString('es-ES');
    
    if (deploymentInProgress) {
        statusBox.innerHTML = `
            <p><strong>Estado:</strong> Despliegue en progreso...</p>
            <p><strong>Última actualización:</strong> ${timestamp}</p>
            <div class="progress-bar">
                <div class="progress-fill"></div>
            </div>
        `;
    } else {
        statusBox.innerHTML = `
            <p><strong>Estado:</strong> Sistema operativo ✓</p>
            <p><strong>Última actualización:</strong> ${timestamp}</p>
            <p><strong>Aplicaciones activas:</strong> 3</p>
            <p><strong>Uptime:</strong> 99.9%</p>
        `;
    }
    
    addLog('[INFO] Estado del sistema consultado', 'info');
}

// Function to simulate application deployment
function deployApplication() {
    if (deploymentInProgress) {
        addLog('[WARNING] Ya hay un despliegue en progreso', 'warning');
        return;
    }
    
    deploymentInProgress = true;
    addLog('[INFO] Iniciando proceso de despliegue...', 'info');
    
    const steps = [
        { message: '[INFO] Validando configuración...', delay: 1000 },
        { message: '[INFO] Construyendo contenedor Docker...', delay: 2000 },
        { message: '[INFO] Ejecutando pruebas...', delay: 1500 },
        { message: '[INFO] Desplegando aplicación...', delay: 2000 },
        { message: '[SUCCESS] ✓ Despliegue completado exitosamente', delay: 1000 }
    ];
    
    let totalDelay = 0;
    steps.forEach((step, index) => {
        totalDelay += step.delay;
        setTimeout(() => {
            const type = step.message.includes('SUCCESS') ? 'success' : 
                        step.message.includes('WARNING') ? 'warning' : 'info';
            addLog(step.message, type);
            
            if (index === steps.length - 1) {
                deploymentInProgress = false;
                showDeploymentStatus();
            }
        }, totalDelay);
    });
    
    showDeploymentStatus();
}

// Function to add log entries
function addLog(message, type = 'info') {
    const logsContainer = document.getElementById('logs');
    const logEntry = document.createElement('p');
    logEntry.className = `log-entry log-${type}`;
    
    const timestamp = new Date().toLocaleTimeString('es-ES');
    logEntry.textContent = `[${timestamp}] ${message}`;
    
    logsContainer.appendChild(logEntry);
    logsContainer.scrollTop = logsContainer.scrollHeight;
    
    // Keep only last 50 log entries
    const logEntries = logsContainer.querySelectorAll('.log-entry');
    if (logEntries.length > 50) {
        logEntries[0].remove();
    }
}

// Smooth scrolling for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Initialize on page load
document.addEventListener('DOMContentLoaded', () => {
    addLog('[INFO] Sistema DevOps Web inicializado', 'info');
    addLog('[INFO] Conectado al servidor de despliegue', 'info');
    addLog('[INFO] Listo para operaciones', 'success');
});

// Simulate periodic status checks
setInterval(() => {
    if (!deploymentInProgress) {
        const statusBox = document.getElementById('deployment-status');
        if (statusBox && statusBox.innerHTML.includes('Sistema operativo')) {
            const timestamp = new Date().toLocaleTimeString('es-ES');
            statusBox.querySelector('p:nth-child(2)').textContent = `Última actualización: ${timestamp}`;
        }
    }
}, 30000); // Update every 30 seconds
