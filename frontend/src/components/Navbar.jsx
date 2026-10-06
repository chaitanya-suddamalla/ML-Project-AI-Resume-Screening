import React from 'react';
import { 
  FileSearch, 
  LayoutDashboard, 
  History, 
  BookOpen, 
  BarChart3, 
  Cpu, 
  ShieldCheck 
} from 'lucide-react';

export default function Navbar({ activeTab, setActiveTab }) {
  const navItems = [
    { id: 'dashboard', label: 'Dashboard', icon: LayoutDashboard },
    { id: 'analyze', label: 'Analyze Resume', icon: FileSearch },
    { id: 'history', label: 'Analysis History', icon: History },
    { id: 'skills', label: 'Skills Catalog', icon: BookOpen },
    { id: 'evaluation', label: 'Model Evaluation', icon: BarChart3 },
  ];

  return (
    <header className="sticky top-0 z-50 glass-panel border-b border-slate-800/80 bg-slate-950/80 backdrop-blur-md">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-16">
          {/* Logo */}
          <div className="flex items-center space-x-3 cursor-pointer" onClick={() => setActiveTab('dashboard')}>
            <div className="p-2 rounded-xl bg-gradient-to-tr from-teal-500 to-emerald-400 text-slate-950 shadow-lg shadow-teal-500/20">
              <Cpu className="w-6 h-6" />
            </div>
            <div>
              <span className="font-display font-bold text-lg text-white tracking-tight flex items-center gap-2">
                ResumeAI <span className="text-xs bg-teal-500/10 text-teal-400 border border-teal-500/20 px-2 py-0.5 rounded-full font-mono">BTech CSE</span>
              </span>
              <p className="text-[11px] text-slate-400 hidden sm:block">AI Resume Screening & Job Matcher</p>
            </div>
          </div>

          {/* Navigation */}
          <nav className="flex space-x-1 sm:space-x-2">
            {navItems.map((item) => {
              const Icon = item.icon;
              const isActive = activeTab === item.id;
              return (
                <button
                  key={item.id}
                  onClick={() => setActiveTab(item.id)}
                  className={`flex items-center space-x-2 px-3 py-2 rounded-lg text-sm font-medium transition-all duration-200 ${
                    isActive
                      ? 'bg-teal-500/15 text-teal-300 border border-teal-500/30 shadow-sm'
                      : 'text-slate-400 hover:text-slate-200 hover:bg-slate-800/50'
                  }`}
                >
                  <Icon className={`w-4 h-4 ${isActive ? 'text-teal-400' : 'text-slate-400'}`} />
                  <span className="hidden md:inline">{item.label}</span>
                </button>
              );
            })}
          </nav>

          {/* Privacy Badge */}
          <div className="hidden xl:flex items-center space-x-2 text-xs text-slate-400 bg-slate-900/60 border border-slate-800 px-3 py-1.5 rounded-full">
            <ShieldCheck className="w-3.5 h-3.5 text-emerald-400" />
            <span>Privacy Preserved (PII Masked)</span>
          </div>
        </div>
      </div>
    </header>
  );
}
