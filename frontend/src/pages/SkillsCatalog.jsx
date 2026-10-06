import React, { useEffect, useState } from 'react';
import { BookOpen, Plus, Search, Tag, Sparkles, Check } from 'lucide-react';
import { api } from '../services/api';

export default function SkillsCatalog() {
  const [catalog, setCatalog] = useState(null);
  const [loading, setLoading] = useState(true);
  const [selectedCategory, setSelectedCategory] = useState('All');
  const [searchTerm, setSearchTerm] = useState('');

  // Add Custom Skill Modal state
  const [showAddModal, setShowAddModal] = useState(false);
  const [newSkillName, setNewSkillName] = useState('');
  const [newSkillCat, setNewSkillCat] = useState('Programming Languages');
  const [newSkillSynonyms, setNewSkillSynonyms] = useState('');
  const [adding, setAdding] = useState(false);
  const [successMsg, setSuccessMsg] = useState('');

  useEffect(() => {
    fetchCatalog();
  }, []);

  const fetchCatalog = async () => {
    setLoading(true);
    try {
      const res = await api.getSkillsCatalog();
      setCatalog(res.data || null);
    } catch (err) {
      console.error("Failed to load skills catalog:", err);
    } finally {
      setLoading(false);
    }
  };

  const handleAddSkill = async (e) => {
    e.preventDefault();
    if (!newSkillName.trim()) return;

    setAdding(true);
    try {
      const synArray = newSkillSynonyms
        .split(',')
        .map((s) => s.trim())
        .filter((s) => s.length > 0);

      await api.addCustomSkill({
        name: newSkillName.trim(),
        category: newSkillCat,
        synonyms: synArray
      });

      setSuccessMsg(`Skill '${newSkillName}' registered successfully!`);
      setNewSkillName('');
      setNewSkillSynonyms('');
      setShowAddModal(false);
      fetchCatalog(); // Refresh catalog
    } catch (err) {
      console.error("Failed to add skill:", err);
      alert("Failed to add skill to dictionary.");
    } finally {
      setAdding(false);
    }
  };

  const categories = catalog?.categories ? Object.keys(catalog.categories) : [];

  return (
    <div className="space-y-8 animate-fadeIn">
      {/* Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <h1 className="text-2xl sm:text-3xl font-display font-bold text-white tracking-tight flex items-center gap-3">
            <BookOpen className="w-7 h-7 text-teal-400" /> Transparent Skill Catalog & Dictionary
          </h1>
          <p className="text-sm text-slate-400">
            Browse normalized technical skills, phrase boundary aliases, and domain learning roadmaps.
          </p>
        </div>
        <button
          onClick={() => setShowAddModal(true)}
          className="inline-flex items-center space-x-2 bg-gradient-to-r from-teal-500 to-emerald-500 hover:from-teal-400 hover:to-emerald-400 text-slate-950 font-semibold px-4 py-2.5 rounded-xl text-xs transition-all shadow-lg shadow-teal-500/20 cursor-pointer"
        >
          <Plus className="w-4 h-4" />
          <span>Add Custom Skill</span>
        </button>
      </div>

      {successMsg && (
        <div className="bg-emerald-500/10 border border-emerald-500/30 rounded-xl p-4 text-emerald-300 text-xs flex items-center gap-2">
          <Check className="w-4 h-4 text-emerald-400" />
          <span>{successMsg}</span>
        </div>
      )}

      {/* Filter and Search Bar */}
      <div className="glass-panel p-4 rounded-2xl border border-slate-800 flex flex-col sm:flex-row items-center justify-between gap-4">
        {/* Category Pills */}
        <div className="flex flex-wrap gap-2">
          <button
            onClick={() => setSelectedCategory('All')}
            className={`px-3 py-1.5 rounded-lg text-xs font-medium transition-all ${
              selectedCategory === 'All'
                ? 'bg-teal-500/20 text-teal-300 border border-teal-500/30'
                : 'bg-slate-900 text-slate-400 hover:text-slate-200'
            }`}
          >
            All Categories
          </button>
          {categories.map((cat) => (
            <button
              key={cat}
              onClick={() => setSelectedCategory(cat)}
              className={`px-3 py-1.5 rounded-lg text-xs font-medium transition-all ${
                selectedCategory === cat
                  ? 'bg-teal-500/20 text-teal-300 border border-teal-500/30'
                  : 'bg-slate-900 text-slate-400 hover:text-slate-200'
              }`}
            >
              {cat}
            </button>
          ))}
        </div>

        {/* Search input */}
        <div className="relative w-full sm:w-64">
          <Search className="w-4 h-4 text-slate-400 absolute left-3 top-3" />
          <input
            type="text"
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            placeholder="Search skills or synonyms..."
            className="bg-slate-950/80 border border-slate-800 text-xs text-white pl-9 pr-4 py-2.5 rounded-xl w-full focus:border-teal-500 focus:outline-none"
          />
        </div>
      </div>

      {/* Skills Grid Grouped by Category */}
      {loading ? (
        <div className="glass-panel p-12 text-center text-slate-400 text-sm">
          Loading transparent dictionary...
        </div>
      ) : (
        <div className="space-y-8">
          {categories
            .filter((cat) => selectedCategory === 'All' || selectedCategory === cat)
            .map((catName) => {
              const skillList = catalog.categories[catName] || [];
              const filteredList = skillList.filter((item) => {
                const term = searchTerm.toLowerCase();
                const matchName = item.name.toLowerCase().includes(term);
                const matchSyn = item.synonyms?.some((s) => s.toLowerCase().includes(term));
                return matchName || matchSyn;
              });

              if (filteredList.length === 0) return null;

              return (
                <div key={catName} className="glass-panel p-6 rounded-2xl border border-slate-800 space-y-4">
                  <div className="flex items-center space-x-2 pb-2 border-b border-slate-800">
                    <Tag className="w-4 h-4 text-teal-400" />
                    <h3 className="font-display font-semibold text-lg text-white">{catName}</h3>
                    <span className="text-xs text-slate-500 font-mono">({filteredList.length} skills)</span>
                  </div>

                  <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                    {filteredList.map((skill, idx) => (
                      <div
                        key={idx}
                        className="bg-slate-900/60 p-4 rounded-xl border border-slate-800/80 hover:border-teal-500/30 transition-all space-y-2"
                      >
                        <div className="flex items-center justify-between">
                          <span className="font-semibold text-sm text-white">{skill.name}</span>
                          <span className="text-[10px] text-teal-400 bg-teal-950/60 px-2 py-0.5 rounded border border-teal-800/40 font-mono">
                            Canonical
                          </span>
                        </div>
                        {skill.synonyms && skill.synonyms.length > 0 && (
                          <div className="text-xs text-slate-400 space-y-1">
                            <span className="text-[10px] text-slate-500 uppercase tracking-wider font-semibold block">Synonyms / Aliases:</span>
                            <div className="flex flex-wrap gap-1">
                              {skill.synonyms.map((syn, si) => (
                                <span key={si} className="text-[11px] bg-slate-800 text-slate-300 px-2 py-0.5 rounded font-mono">
                                  {syn}
                                </span>
                              ))}
                            </div>
                          </div>
                        )}
                      </div>
                    ))}
                  </div>
                </div>
              );
            })}
        </div>
      )}

      {/* Add Skill Modal */}
      {showAddModal && (
        <div className="fixed inset-0 z-50 bg-slate-950/80 backdrop-blur-sm flex items-center justify-center p-4">
          <div className="glass-panel max-w-lg w-full p-6 rounded-2xl border border-slate-800 space-y-4">
            <h3 className="text-lg font-display font-bold text-white flex items-center gap-2">
              <Sparkles className="w-5 h-5 text-teal-400" /> Register Custom Skill to Dictionary
            </h3>
            <p className="text-xs text-slate-400">
              Expand the transparent skill catalog. New skills are immediately recognized by the NLP phrase extraction engine.
            </p>

            <form onSubmit={handleAddSkill} className="space-y-4">
              <div>
                <label className="text-xs text-slate-300 font-medium block mb-1">Standard Skill Name</label>
                <input
                  type="text"
                  required
                  value={newSkillName}
                  onChange={(e) => setNewSkillName(e.target.value)}
                  placeholder="e.g. GraphQL, Rust, PyTorch"
                  className="w-full bg-slate-950/80 border border-slate-800 rounded-lg p-2.5 text-xs text-white focus:border-teal-500 focus:outline-none"
                />
              </div>

              <div>
                <label className="text-xs text-slate-300 font-medium block mb-1">Category</label>
                <select
                  value={newSkillCat}
                  onChange={(e) => setNewSkillCat(e.target.value)}
                  className="w-full bg-slate-950/80 border border-slate-800 rounded-lg p-2.5 text-xs text-white focus:border-teal-500 focus:outline-none"
                >
                  {categories.map((c) => (
                    <option key={c} value={c}>{c}</option>
                  ))}
                  <option value="Custom Skill Category">Custom Skill Category</option>
                </select>
              </div>

              <div>
                <label className="text-xs text-slate-300 font-medium block mb-1">Synonyms / Variations (Comma separated)</label>
                <input
                  type="text"
                  value={newSkillSynonyms}
                  onChange={(e) => setNewSkillSynonyms(e.target.value)}
                  placeholder="e.g. graphql api, gql"
                  className="w-full bg-slate-950/80 border border-slate-800 rounded-lg p-2.5 text-xs text-white focus:border-teal-500 focus:outline-none"
                />
              </div>

              <div className="flex justify-end space-x-3 pt-2">
                <button
                  type="button"
                  onClick={() => setShowAddModal(false)}
                  className="px-4 py-2 rounded-lg text-xs text-slate-400 hover:bg-slate-800"
                >
                  Cancel
                </button>
                <button
                  type="submit"
                  disabled={adding}
                  className="px-4 py-2 rounded-lg text-xs bg-teal-500 hover:bg-teal-400 text-slate-950 font-semibold shadow-lg shadow-teal-500/20 cursor-pointer"
                >
                  {adding ? 'Saving...' : 'Add Skill'}
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
}
