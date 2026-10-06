import React, { useEffect, useState } from 'react';
import { 
  History as HistoryIcon, 
  Trash2, 
  Eye, 
  Search, 
  X, 
  CheckCircle2, 
  XCircle, 
  Building2, 
  Calendar,
  AlertCircle
} from 'lucide-react';
import { api } from '../services/api';
import SkillBadge from '../components/SkillBadge';
import ChecklistTable from '../components/ChecklistTable';

export default function HistoryPage() {
  const [analyses, setAnalyses] = useState([]);
  const [loading, setLoading] = useState(true);
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedAnalysis, setSelectedAnalysis] = useState(null);
  const [deleteConfirmId, setDeleteConfirmId] = useState(null);

  useEffect(() => {
    fetchHistory();
  }, []);

  const fetchHistory = async () => {
    setLoading(true);
    try {
      const res = await api.getAnalyses();
      setAnalyses(res.data || []);
    } catch (err) {
      console.error("Failed to load analysis history:", err);
    } finally {
      setLoading(false);
    }
  };

  const handleDelete = async (id) => {
    try {
      await api.deleteAnalysis(id);
      setAnalyses(analyses.filter((item) => item.id !== id));
      if (selectedAnalysis?.id === id) {
        setSelectedAnalysis(null);
      }
      setDeleteConfirmId(null);
    } catch (err) {
      console.error("Failed to delete analysis:", err);
      alert("Failed to delete record.");
    }
  };

  const filtered = analyses.filter((item) => {
    const term = searchTerm.toLowerCase();
    return (
      item.job_title.toLowerCase().includes(term) ||
      (item.company_name && item.company_name.toLowerCase().includes(term))
    );
  });

  return (
    <div className="space-y-8 animate-fadeIn">
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <h1 className="text-2xl sm:text-3xl font-display font-bold text-white tracking-tight flex items-center gap-3">
            <HistoryIcon className="w-7 h-7 text-teal-400" /> Stored Analysis History
          </h1>
          <p className="text-sm text-slate-400">
            Review past resume evaluations, skill match records, and saved learning checklist items.
          </p>
        </div>
        <div className="relative">
          <Search className="w-4 h-4 text-slate-400 absolute left-3 top-3" />
          <input
            type="text"
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            placeholder="Search job title or company..."
            className="bg-slate-950/80 border border-slate-800 text-xs text-white pl-9 pr-4 py-2.5 rounded-xl w-64 focus:border-teal-500 focus:outline-none"
          />
        </div>
      </div>

      {loading ? (
        <div className="glass-panel p-12 text-center text-slate-400 text-sm">
          Loading stored history...
        </div>
      ) : filtered.length === 0 ? (
        <div className="glass-panel p-12 text-center space-y-3 rounded-2xl border border-slate-800">
          <AlertCircle className="w-10 h-10 text-slate-600 mx-auto" />
          <p className="text-sm text-slate-400">No matching analysis records found in database.</p>
        </div>
      ) : (
        <div className="glass-panel rounded-2xl border border-slate-800 overflow-hidden">
          <div className="overflow-x-auto">
            <table className="w-full text-left text-sm text-slate-300">
              <thead className="text-xs uppercase bg-slate-900/80 text-slate-400 border-b border-slate-800">
                <tr>
                  <th className="py-3.5 px-4 font-semibold">ID</th>
                  <th className="py-3.5 px-4 font-semibold">Target Position</th>
                  <th className="py-3.5 px-4 font-semibold">Company</th>
                  <th className="py-3.5 px-4 font-semibold">TF-IDF Score</th>
                  <th className="py-3.5 px-4 font-semibold">Matched</th>
                  <th className="py-3.5 px-4 font-semibold">Missing</th>
                  <th className="py-3.5 px-4 font-semibold">Date</th>
                  <th className="py-3.5 px-4 font-semibold text-right">Actions</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-slate-800/60">
                {filtered.map((item) => (
                  <tr key={item.id} className="hover:bg-slate-800/30 transition-colors">
                    <td className="py-4 px-4 font-mono text-xs text-slate-500">#{item.id}</td>
                    <td className="py-4 px-4 font-semibold text-white">{item.job_title}</td>
                    <td className="py-4 px-4 text-xs text-slate-400">{item.company_name || 'N/A'}</td>
                    <td className="py-4 px-4 font-mono font-bold text-teal-400">
                      {item.similarity_percentage}%
                    </td>
                    <td className="py-4 px-4 text-xs text-emerald-400 font-mono">
                      {item.matched_skills?.length || 0} skills
                    </td>
                    <td className="py-4 px-4 text-xs text-amber-400 font-mono">
                      {item.missing_skills?.length || 0} skills
                    </td>
                    <td className="py-4 px-4 text-xs text-slate-500 font-mono">
                      {new Date(item.created_at).toLocaleDateString()}
                    </td>
                    <td className="py-4 px-4 text-right space-x-2">
                      <button
                        onClick={() => setSelectedAnalysis(item)}
                        className="p-1.5 rounded-lg bg-teal-500/10 text-teal-400 hover:bg-teal-500/20 transition-colors cursor-pointer"
                        title="View Full Analysis Details"
                      >
                        <Eye className="w-4 h-4" />
                      </button>
                      <button
                        onClick={() => setDeleteConfirmId(item.id)}
                        className="p-1.5 rounded-lg bg-rose-500/10 text-rose-400 hover:bg-rose-500/20 transition-colors cursor-pointer"
                        title="Delete Analysis Record"
                      >
                        <Trash2 className="w-4 h-4" />
                      </button>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      )}

      {/* Delete Confirmation Modal */}
      {deleteConfirmId && (
        <div className="fixed inset-0 z-50 bg-slate-950/80 backdrop-blur-sm flex items-center justify-center p-4">
          <div className="glass-panel max-w-md w-full p-6 rounded-2xl border border-rose-500/30 space-y-4">
            <h3 className="text-lg font-display font-bold text-white flex items-center gap-2">
              <Trash2 className="w-5 h-5 text-rose-400" /> Confirm Deletion
            </h3>
            <p className="text-xs text-slate-300">
              Are you sure you want to delete analysis record #{deleteConfirmId}? This will permanently remove its persistent learning checklist records.
            </p>
            <div className="flex justify-end space-x-3 pt-2">
              <button
                onClick={() => setDeleteConfirmId(null)}
                className="px-4 py-2 rounded-lg text-xs text-slate-400 hover:bg-slate-800"
              >
                Cancel
              </button>
              <button
                onClick={() => handleDelete(deleteConfirmId)}
                className="px-4 py-2 rounded-lg text-xs bg-rose-500 hover:bg-rose-600 text-white font-semibold shadow-lg shadow-rose-500/20"
              >
                Delete Record
              </button>
            </div>
          </div>
        </div>
      )}

      {/* Detail View Modal */}
      {selectedAnalysis && (
        <div className="fixed inset-0 z-50 bg-slate-950/80 backdrop-blur-sm flex items-center justify-center p-4 overflow-y-auto">
          <div className="glass-panel max-w-4xl w-full p-6 rounded-2xl border border-slate-800 space-y-6 max-h-[90vh] overflow-y-auto">
            <div className="flex items-center justify-between pb-4 border-b border-slate-800">
              <div>
                <h3 className="text-xl font-display font-bold text-white">
                  {selectedAnalysis.job_title}
                </h3>
                <p className="text-xs text-slate-400 flex items-center gap-2 mt-1">
                  <Building2 className="w-3.5 h-3.5 text-teal-400" /> {selectedAnalysis.company_name || 'General Role'} &bull;
                  <Calendar className="w-3.5 h-3.5 text-teal-400" /> {new Date(selectedAnalysis.created_at).toLocaleString()}
                </p>
              </div>
              <button
                onClick={() => setSelectedAnalysis(null)}
                className="p-2 text-slate-400 hover:text-white rounded-lg bg-slate-900 border border-slate-800"
              >
                <X className="w-5 h-5" />
              </button>
            </div>

            {/* Score metric summary */}
            <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
              <div className="bg-slate-900/60 p-4 rounded-xl border border-slate-800 text-center">
                <span className="text-xs text-slate-400">Similarity Match</span>
                <p className="text-2xl font-bold font-mono text-teal-400 mt-1">
                  {selectedAnalysis.similarity_percentage}%
                </p>
              </div>
              <div className="bg-slate-900/60 p-4 rounded-xl border border-slate-800 text-center">
                <span className="text-xs text-slate-400">Matched Skills</span>
                <p className="text-2xl font-bold font-mono text-emerald-400 mt-1">
                  {selectedAnalysis.matched_skills.length}
                </p>
              </div>
              <div className="bg-slate-900/60 p-4 rounded-xl border border-slate-800 text-center">
                <span className="text-xs text-slate-400">Missing Gaps</span>
                <p className="text-2xl font-bold font-mono text-amber-400 mt-1">
                  {selectedAnalysis.missing_skills.length}
                </p>
              </div>
            </div>

            {/* Skills Badges */}
            <div className="space-y-3">
              <h4 className="text-sm font-semibold text-white">Matched Skills:</h4>
              <div className="flex flex-wrap gap-2">
                {selectedAnalysis.matched_skills.map((s, i) => (
                  <SkillBadge key={i} skill={s} type="matched" />
                ))}
              </div>

              <h4 className="text-sm font-semibold text-white pt-2">Missing Skills:</h4>
              <div className="flex flex-wrap gap-2">
                {selectedAnalysis.missing_skills.map((s, i) => (
                  <SkillBadge key={i} skill={s} type="missing" />
                ))}
              </div>
            </div>

            {/* Checklist items */}
            {selectedAnalysis.learning_checklist && selectedAnalysis.learning_checklist.length > 0 && (
              <ChecklistTable items={selectedAnalysis.learning_checklist} />
            )}
          </div>
        </div>
      )}
    </div>
  );
}
