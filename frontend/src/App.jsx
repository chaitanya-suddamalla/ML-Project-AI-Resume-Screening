import React, { useState } from 'react';
import Navbar from './components/Navbar';
import Footer from './components/Footer';
import Dashboard from './pages/Dashboard';
import Analyze from './pages/Analyze';
import History from './pages/History';
import SkillsCatalog from './pages/SkillsCatalog';
import ModelEvaluation from './pages/ModelEvaluation';

export default function App() {
  const [activeTab, setActiveTab] = useState('dashboard');

  const renderActiveTab = () => {
    switch (activeTab) {
      case 'dashboard':
        return <Dashboard setActiveTab={setActiveTab} />;
      case 'analyze':
        return <Analyze />;
      case 'history':
        return <History />;
      case 'skills':
        return <SkillsCatalog />;
      case 'evaluation':
        return <ModelEvaluation />;
      default:
        return <Dashboard setActiveTab={setActiveTab} />;
    }
  };

  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 flex flex-col font-sans">
      <Navbar activeTab={activeTab} setActiveTab={setActiveTab} />
      
      <main className="flex-grow max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {renderActiveTab()}
      </main>

      <Footer />
    </div>
  );
}
