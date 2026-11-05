import React, { useState } from 'react';
import { Search, Sparkles, GitFork, HelpCircle } from 'lucide-react';
import { Header, type NavTab } from './components/Header';
import { Footer } from './components/Footer';
import { MetricCard } from './components/MetricCard';
import { MetricDetailView } from './components/MetricDetailView';
import { MethodWarningBanner } from './components/MethodWarningBanner';
import { MethodDivergenceDemo } from './components/MethodDivergenceDemo';
import { FitForPurposeWizard } from './components/FitForPurposeWizard';
import { useCatalog, useMetric } from './hooks/useMetricData';

export const App: React.FC = () => {
  const { data: catalog, loading: catalogLoading, error: catalogError } = useCatalog();
  const [activeTab, setActiveTab] = useState<NavTab>('catalog');
  const [selectedMetricId, setSelectedMetricId] = useState<string | null>(null);
  const [searchQuery, setSearchQuery] = useState<string>('');
  const [selectedCategory, setSelectedCategory] = useState<string>('All');
  const [showAvailableOnly, setShowAvailableOnly] = useState<boolean>(false);

  const { data: activeMetric, loading: metricLoading, error: metricError } = useMetric(selectedMetricId);

  const categories = React.useMemo(() => {
    if (!catalog) return ['All'];
    const cats = Array.from(new Set(catalog.metrics.map((m) => m.category)));
    return ['All', ...cats.sort()];
  }, [catalog]);

  const filteredMetrics = React.useMemo(() => {
    if (!catalog) return [];
    return catalog.metrics.filter((m) => {
      if (showAvailableOnly && m.status !== 'available') return false;
      if (selectedCategory !== 'All' && m.category !== selectedCategory) return false;
      if (searchQuery.trim() !== '') {
        const q = searchQuery.toLowerCase();
        return (
          m.name.toLowerCase().includes(q) ||
          m.definition.toLowerCase().includes(q) ||
          m.category.toLowerCase().includes(q) ||
          (m.academy_module && m.academy_module.toLowerCase().includes(q))
        );
      }
      return true;
    });
  }, [catalog, showAvailableOnly, selectedCategory, searchQuery]);

  return (
    <div className="min-h-screen flex flex-col bg-[var(--color-plane)] text-[var(--color-ink)] transition-colors">
      <Header
        activeTab={activeTab}
        onTabChange={setActiveTab}
        onSelectMetric={setSelectedMetricId}
      />

      <main className="flex-1 mx-auto max-w-7xl px-4 py-8 sm:px-6 lg:px-8 w-full">
        {selectedMetricId && activeMetric ? (
          <div>
            {metricLoading ? (
              <div className="py-20 text-center text-sm text-[var(--color-ink-muted)]">
                Loading metric distributions...
              </div>
            ) : metricError ? (
              <div className="py-20 text-center text-sm text-[var(--color-critical)]">
                Failed to load metric data: {metricError}
              </div>
            ) : (
              <MetricDetailView
                metric={activeMetric}
                onBack={() => setSelectedMetricId(null)}
              />
            )}
          </div>
        ) : activeTab === 'divergence' ? (
          <div className="space-y-8">
            <MethodDivergenceDemo />
            <FitForPurposeWizard />
          </div>
        ) : activeTab === 'wizard' ? (
          <div className="space-y-8">
            <FitForPurposeWizard />
            <MethodDivergenceDemo />
          </div>
        ) : (
          <div className="space-y-12">
            {/* Hero Section */}
            <div className="rounded-3xl border border-[var(--color-grid)] bg-[var(--color-surface)] p-6 sm:p-10 shadow-xs relative overflow-hidden">
              <div className="max-w-3xl space-y-4">
                <div className="inline-flex items-center gap-1.5 rounded-full border border-[var(--color-series-1)]/30 bg-[var(--color-series-1)]/10 px-3 py-1 text-xs font-semibold text-[var(--color-series-1)]">
                  <Sparkles className="h-3.5 w-3.5" />
                  <span>The Population Truth &bull; Epistemological Reference Engine</span>
                </div>

                <h1 className="text-3xl sm:text-4xl lg:text-5xl font-black tracking-tight text-[var(--color-ink)] leading-tight">
                  Empirical Physiological Distributions for Study Design &amp; Device Validation
                </h1>

                <p className="text-base sm:text-lg leading-relaxed text-[var(--color-ink-secondary)]">
                  What does physiological spread actually look like across human bodies? Health Data Distributions provides
                  reproducible population percentiles, between-subject variation (&sigma;<sub>b</sub>), and expert guidance on{' '}
                  <strong className="text-[var(--color-ink)]">when and when NOT to pool</strong> disparate datasets together.
                </p>

                {/* Method Warning Banner */}
                <div className="pt-2">
                  <MethodWarningBanner
                    warning="A clinic pulse, an ECG Holter, and a wearable's overnight resting heart rate are systematically distinct distributions. Never pool across disparate measurement protocols or apply hierarchical shrinkage across protected physical covariates."
                  />
                </div>

                <div className="pt-2 flex flex-wrap gap-2 text-xs">
                  <button
                    type="button"
                    onClick={() => setActiveTab('divergence')}
                    className="inline-flex items-center gap-1.5 rounded-lg bg-[var(--color-warning)]/10 border border-[var(--color-warning)]/30 px-3 py-1.5 font-bold text-[var(--color-warning)] hover:bg-[var(--color-warning)]/15 transition-colors"
                  >
                    <GitFork className="h-3.5 w-3.5" />
                    <span>See Why Method Matters (Interactive Demo) &rarr;</span>
                  </button>
                  <button
                    type="button"
                    onClick={() => setActiveTab('wizard')}
                    className="inline-flex items-center gap-1.5 rounded-lg bg-[var(--color-series-1)]/10 border border-[var(--color-series-1)]/30 px-3 py-1.5 font-bold text-[var(--color-series-1)] hover:bg-[var(--color-series-1)]/15 transition-colors"
                  >
                    <HelpCircle className="h-3.5 w-3.5" />
                    <span>Fit-for-Purpose Protocol Wizard &rarr;</span>
                  </button>
                </div>
              </div>

              {/* Stats Bar */}
              <div className="mt-8 grid grid-cols-2 gap-4 border-t border-[var(--color-grid)] pt-6 sm:grid-cols-4">
                <div>
                  <div className="text-2xl font-black font-mono text-[var(--color-ink)]">15</div>
                  <div className="text-xs uppercase font-semibold text-[var(--color-ink-muted)]">Target Metrics</div>
                </div>
                <div>
                  <div className="text-2xl font-black font-mono text-[var(--color-series-1)]">103,305+</div>
                  <div className="text-xs uppercase font-semibold text-[var(--color-ink-muted)]">Examined Subjects</div>
                </div>
                <div>
                  <div className="text-2xl font-black font-mono text-[var(--color-series-2)]">MST 1–10</div>
                  <div className="text-xs uppercase font-semibold text-[var(--color-ink-muted)]">Monk Skin Scale</div>
                </div>
                <div>
                  <div className="text-2xl font-black font-mono text-[var(--color-series-3)]">100%</div>
                  <div className="text-xs uppercase font-semibold text-[var(--color-ink-muted)]">Open JSON &amp; CSV</div>
                </div>
              </div>
            </div>

            {/* Filter and Search Bar */}
            <div className="flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between">
              <div className="relative flex-1 max-w-md">
                <Search className="absolute left-3 top-1/2 h-4 w-4 -translate-y-1/2 text-[var(--color-ink-muted)]" />
                <input
                  type="text"
                  value={searchQuery}
                  onChange={(e) => setSearchQuery(e.target.value)}
                  placeholder="Search metrics, categories, Academy modules..."
                  className="w-full rounded-xl border border-[var(--color-grid)] bg-[var(--color-surface)] pl-9 pr-4 py-2 text-xs text-[var(--color-ink)] placeholder-[var(--color-ink-muted)] shadow-xs transition-colors focus:border-[var(--color-series-1)]"
                />
              </div>

              <div className="flex flex-wrap items-center gap-2">
                <button
                  type="button"
                  onClick={() => setShowAvailableOnly(!showAvailableOnly)}
                  className={`rounded-lg px-3 py-1.5 text-xs font-semibold transition-all ${
                    showAvailableOnly
                      ? 'bg-[var(--color-good)] text-white shadow-xs'
                      : 'border border-[var(--color-grid)] bg-[var(--color-surface)] text-[var(--color-ink-secondary)] hover:bg-[var(--color-surface-subtle)]'
                  }`}
                >
                  {showAvailableOnly ? '✓ Available Only' : 'Show All (incl. Planned)'}
                </button>
              </div>
            </div>

            {/* Category Filter Pills */}
            <div className="flex flex-wrap gap-1.5 border-b border-[var(--color-grid)] pb-3">
              {categories.map((cat) => (
                <button
                  key={cat}
                  type="button"
                  onClick={() => setSelectedCategory(cat)}
                  className={`rounded-lg px-3 py-1.5 text-xs font-semibold transition-colors ${
                    selectedCategory === cat
                      ? 'bg-[var(--color-ink)] text-[var(--color-surface)] shadow-xs'
                      : 'bg-[var(--color-surface)] text-[var(--color-ink-secondary)] border border-[var(--color-grid)] hover:bg-[var(--color-surface-subtle)]'
                  }`}
                >
                  {cat}
                </button>
              ))}
            </div>

            {/* Metrics Catalog Grid */}
            {catalogLoading ? (
              <div className="py-20 text-center text-sm text-[var(--color-ink-muted)]">
                Loading catalog index...
              </div>
            ) : catalogError ? (
              <div className="py-20 text-center text-sm text-[var(--color-critical)]">
                Failed to load catalog: {catalogError}
              </div>
            ) : filteredMetrics.length === 0 ? (
              <div className="py-20 text-center text-sm text-[var(--color-ink-muted)]">
                No metrics match the selected filter.
              </div>
            ) : (
              <div className="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3">
                {filteredMetrics.map((metric) => (
                  <MetricCard
                    key={metric.id}
                    metric={metric}
                    onSelect={(id) => setSelectedMetricId(id)}
                  />
                ))}
              </div>
            )}
          </div>
        )}
      </main>

      <Footer />
    </div>
  );
};
