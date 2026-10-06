import React from 'react';
import { Award, AlertCircle, Info, Sparkles, CheckCircle2 } from 'lucide-react';

export default function SimilarityGauge({ similarity, keywordBaseline }) {
  const percentage = similarity?.percentage || 0;
  const level = similarity?.level || 'Low Similarity';

  // Determine theme color based on score
  let colorClass = 'text-amber-400 bg-amber-500/10 border-amber-500/30';
  let strokeColor = '#f59e0b';
  if (percentage >= 75) {
    colorClass = 'text-emerald-400 bg-emerald-500/10 border-emerald-500/30';
    strokeColor = '#10b981';
  } else if (percentage >= 50) {
    colorClass = 'text-teal-400 bg-teal-500/10 border-teal-500/30';
    strokeColor = '#14b8a6';
  } else if (percentage >= 30) {
    colorClass = 'text-amber-400 bg-amber-500/10 border-amber-500/30';
    strokeColor = '#f59e0b';
  } else {
    colorClass = 'text-rose-400 bg-rose-500/10 border-rose-500/30';
    strokeColor = '#f43f5e';
  }

  const circumference = 2 * Math.PI * 52;
  const strokeDashoffset = circumference - (percentage / 100) * circumference;

  return (
    <div className="glass-panel p-6 rounded-2xl border border-slate-800 space-y-6">
      <div className="flex items-center justify-between">
        <div className="flex items-center space-x-2">
          <Sparkles className="w-5 h-5 text-teal-400" />
          <h3 className="font-display font-semibold text-lg text-white">TF-IDF Vector Cosine Similarity</h3>
        </div>
        <span className={`text-xs px-3 py-1 rounded-full font-medium border ${colorClass}`}>
          {level}
        </span>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 items-center">
        {/* Radial Gauge */}
        <div className="flex flex-col items-center justify-center relative py-2">
          <div className="relative w-36 h-36 flex items-center justify-center">
            <svg className="w-full h-full transform -rotate-90" viewBox="0 0 120 120">
              <circle
                cx="60"
                cy="60"
                r="52"
                className="stroke-slate-800"
                strokeWidth="10"
                fill="transparent"
              />
              <circle
                cx="60"
                cy="60"
                r="52"
                stroke={strokeColor}
                strokeWidth="10"
                fill="transparent"
                strokeDasharray={circumference}
                strokeDashoffset={strokeDashoffset}
                strokeLinecap="round"
                className="transition-all duration-1000 ease-out"
              />
            </svg>
            <div className="absolute flex flex-col items-center">
              <span className="text-3xl font-display font-extrabold text-white tracking-tight">
                {percentage}%
              </span>
              <span className="text-[10px] text-slate-400 font-medium tracking-wider uppercase">Match Score</span>
            </div>
          </div>
        </div>

        {/* Breakdown details */}
        <div className="md:col-span-2 space-y-4">
          <div className="bg-slate-900/60 p-4 rounded-xl border border-slate-800 space-y-3">
            <div className="flex justify-between items-center text-xs">
              <span className="text-slate-400 font-medium">Metric Type:</span>
              <span className="text-teal-300 font-mono">TF-IDF N-gram Vector Cosine Angle</span>
            </div>
            {keywordBaseline !== undefined && (
              <div className="flex justify-between items-center text-xs">
                <span className="text-slate-400 font-medium">Jaccard Keyword Baseline:</span>
                <span className="text-slate-300 font-mono">{(keywordBaseline * 100).toFixed(1)}%</span>
              </div>
            )}
            <div className="w-full bg-slate-800 h-2 rounded-full overflow-hidden">
              <div 
                className="bg-gradient-to-r from-teal-500 to-emerald-400 h-full rounded-full transition-all duration-700" 
                style={{ width: `${percentage}%` }}
              />
            </div>
          </div>

          <div className="text-xs text-slate-400 space-y-1">
            <p className="flex items-center gap-1.5 text-slate-300 font-medium">
              <Info className="w-3.5 h-3.5 text-teal-400 flex-shrink-0" />
              Score Interpretation Guide
            </p>
            <p className="leading-relaxed pl-5">
              Reflects the mathematical vector alignment between resume terms and job requirements.
              High scores indicate aligned technical vocabulary, not an automated hiring promise.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}
