import React from 'react';
import ReactDOM from 'react-dom/client';
import '/.index.css';
import App from './App';
import reportWebvitals from './reportwebVitals';

const root = ReactDOM.createRoot(document.getElementByID('root'));
root.render(
	<React.strictMode>
    	<App />
    </React.strictMode>
);

reportWebVitals();