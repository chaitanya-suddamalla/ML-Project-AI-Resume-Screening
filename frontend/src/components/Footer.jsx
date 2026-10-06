import React from 'react';
import { AlertTriangle, Info, Github, BookOpen } from 'lucide-react';

export default function Footer() {
  return (
    <footer className="glass-panel border-t border-slate-800/80 mt-auto py-8 text-slate-400 text-sm">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-6">
        {/* Disclaimer Banner */}
        <div className="bg-amber-500/10 border border-amber-500/30 rounded-xl p-4 flex items-start space-x-3 text-amber-200">
          <AlertTriangle className="w-5 h-5 text-amber-400 flex-shrink-0 mt-0.5" />
          <div className="text-xs sm:text-sm leading-relaxed">
            <strong className="font-semibold block text-amber-300 mb-1">Career Assistance & Educational Tool Disclaimer</strong>
            This system evaluates TF-IDF vocabulary overlap and phrase similarity to assist students in recognizing skill gaps. It does <strong>NOT</strong> calculate hiring probabilities, measure work ethic, or substitute human recruitment decisions. It strictly adheres to ethical NLP guidelines without inferring protected candidate traits.
          </div>
        </div>

        {/* Footer bottom bar */}
        <div className="flex flex-col sm:flex-row items-center justify-between pt-4 border-t border-slate-800 text-xs text-slate-500 gap-4">
          <div>
            AI-Based Resume Screening and Job Matching System &bull; BTech CSE Final Year Capstone Project
          </div>
          <div className="flex items-center space-x-6">
            <span className="flex items-center gap-1 hover:text-slate-300 transition-colors cursor-pointer">
              <Info className="w-3.5 h-3.5 text-teal-400" /> NLP Pipeline v1.0
            </span>
            <span className="flex items-center gap-1 hover:text-slate-300 transition-colors cursor-pointer">
              <BookOpen className="w-3.5 h-3.5 text-teal-400" /> Transparent Skill Dict
            </span>
          </div>
        </div>
      </div>
    </footer>
  );
}
