import React, { useState } from 'react';
import { CheckCircle2, Clock, Circle, BookOpen, Rocket, ShieldAlert } from 'lucide-react';
import { api } from '../services/api';

export default function ChecklistTable({ items = [], onStatusUpdate }) {
  const [loadingItemId, setLoadingItemId] = useState(null);

  const handleStatusChange = async (item, newStatus) => {
    if (item.status === newStatus) return;
    setLoadingItemId(item.id);
    try {
      await api.updateChecklistItemStatus(item.id, newStatus);
      if (onStatusUpdate) {
        onStatusUpdate(item.id, newStatus);
      }
    } catch (err) {
      console.error("Failed to update status:", err);
      alert("Failed to update skill status. Please try again.");
    } finally {
      setLoadingItemId(null);
    }
  };

  if (!items || items.length === 0) {
    return (
      <div className="glass-panel p-8 text-center rounded-2xl border border-slate-800 space-y-3">
        <CheckCircle2 className="w-12 h-12 text-emerald-400 mx-auto" />
        <h4 className="text-base font-semibold text-white">No Missing Skill Gaps Identified!</h4>
        <p className="text-xs text-slate-400 max-w-md mx-auto">
          The candidate resume includes all required technical skills listed in the target job posting.
        </p>
      </div>
    );
  }

  return (
    <div className="glass-panel rounded-2xl border border-slate-800 overflow-hidden space-y-4 p-6">
      <div className="flex items-center justify-between pb-2 border-b border-slate-800">
        <div>
          <h3 className="font-display font-semibold text-lg text-white flex items-center gap-2">
            <Rocket className="w-5 h-5 text-amber-400" /> Personalized Skill Roadmap & Action Plan
          </h3>
          <p className="text-xs text-slate-400">
            Actionable project exercises designed to close missing skill gaps for this job role.
          </p>
        </div>
        <span className="text-xs font-mono text-amber-400 bg-amber-500/10 px-3 py-1 rounded-full border border-amber-500/20">
          {items.length} Action Items
        </span>
      </div>

      <div className="overflow-x-auto">
        <table className="w-full text-left text-sm text-slate-300">
          <thead className="text-xs uppercase bg-slate-900/80 text-slate-400 border-b border-slate-800">
            <tr>
              <th className="py-3 px-4 font-semibold">Missing Skill</th>
              <th className="py-3 px-4 font-semibold">Job Relevance Context</th>
              <th className="py-3 px-4 font-semibold">Suggested Practice Project</th>
              <th className="py-3 px-4 font-semibold">Level</th>
              <th className="py-3 px-4 font-semibold text-center">Status Tracking</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-slate-800/60">
            {items.map((item) => {
              const isUpdating = loadingItemId === item.id;
              
              let levelBadge = "bg-blue-500/10 text-blue-400 border-blue-500/20";
              if (item.proficiency_level === "Advanced") {
                levelBadge = "bg-rose-500/10 text-rose-400 border-rose-500/20";
              } else if (item.proficiency_level === "Intermediate") {
                levelBadge = "bg-amber-500/10 text-amber-400 border-amber-500/20";
              }

              return (
                <tr key={item.id || item.item_id} className="hover:bg-slate-800/30 transition-colors">
                  <td className="py-4 px-4 font-semibold text-white align-top">
                    <div className="flex flex-col">
                      <span>{item.skill_name}</span>
                      <span className="text-[10px] text-slate-500 font-mono font-normal">{item.category}</span>
                    </div>
                  </td>
                  <td className="py-4 px-4 text-xs text-slate-300 align-top max-w-xs leading-relaxed">
                    {item.relevance_explanation}
                  </td>
                  <td className="py-4 px-4 text-xs text-slate-300 align-top max-w-sm leading-relaxed">
                    <div className="bg-slate-900/50 p-2.5 rounded-lg border border-slate-800 text-slate-200 font-mono text-[11px]">
                      {item.suggested_project}
                    </div>
                  </td>
                  <td className="py-4 px-4 align-top">
                    <span className={`text-[10px] font-mono px-2 py-0.5 rounded border ${levelBadge}`}>
                      {item.proficiency_level}
                    </span>
                  </td>
                  <td className="py-4 px-4 align-top text-center">
                    <div className="inline-flex rounded-lg p-1 bg-slate-900 border border-slate-800 space-x-1">
                      <button
                        onClick={() => handleStatusChange(item, 'Not Started')}
                        disabled={isUpdating}
                        className={`px-2 py-1 rounded text-[11px] font-medium transition-all ${
                          item.status === 'Not Started'
                            ? 'bg-rose-500/20 text-rose-300 border border-rose-500/30'
                            : 'text-slate-500 hover:text-slate-300'
                        }`}
                      >
                        Not Started
                      </button>
                      <button
                        onClick={() => handleStatusChange(item, 'In Progress')}
                        disabled={isUpdating}
                        className={`px-2 py-1 rounded text-[11px] font-medium transition-all ${
                          item.status === 'In Progress'
                            ? 'bg-amber-500/20 text-amber-300 border border-amber-500/30'
                            : 'text-slate-500 hover:text-slate-300'
                        }`}
                      >
                        In Progress
                      </button>
                      <button
                        onClick={() => handleStatusChange(item, 'Completed')}
                        disabled={isUpdating}
                        className={`px-2 py-1 rounded text-[11px] font-medium transition-all ${
                          item.status === 'Completed'
                            ? 'bg-emerald-500/20 text-emerald-300 border border-emerald-500/30'
                            : 'text-slate-500 hover:text-slate-300'
                        }`}
                      >
                        Completed
                      </button>
                    </div>
                  </td>
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>
    </div>
  );
}
