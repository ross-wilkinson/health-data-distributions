import React, { useState, useEffect } from 'react';
import { Activity, Moon, Sun, ExternalLink, GraduationCap, GitFork, HelpCircle } from 'lucide-react';

export type NavTab = 'catalog' | 'divergence' | 'wizard';

interface HeaderProps {
  activeTab: NavTab;
  onTabChange: (tab: NavTab) => void;
  onSelectMetric?: (id: string | null) => void;
}

export const Header: React.FC<HeaderProps> = ({ activeTab, onTabChange, onSelectMetric }) => {
  const [theme, setTheme] = useState<'light' | 'dark'>('light');

  useEffect(() => {
    const isDark =
      document.documentElement.getAttribute('data-theme') === 'dark' ||
      (!('data-theme' in document.documentElement.dataset) &&
        window.matchMedia('(prefers-color-scheme: dark)').matches);
    setTheme(isDark ? 'dark' : 'light');
  }, []);

  const toggleTheme = () => {
    const next = theme === 'dark' ? 'light' : 'dark';
    setTheme(next);
    document.documentElement.setAttribute('data-theme', next);
  };

  return (
    <header className="sticky top-0 z-40 w-full border-b border-[var(--color-grid)] bg-[var(--color-surface)]/90 backdrop-blur-md transition-colors">
      <div className="mx-auto flex max-w-7xl items-center justify-between px-4 py-3 sm:px-6 lg:px-8">
        <button
          type="button"
          onClick={() => {
            onTabChange('catalog');
            onSelectMetric?.(null);
          }}
          className="flex items-center gap-3 text-left transition-opacity hover:opacity-85"
        >
          <div className="flex h-9 w-9 items-center justify-center rounded-lg bg-[var(--color-series-1)]/10 text-[var(--color-series-1)] font-bold shadow-xs">
            <Activity className="h-5 w-5" />
          </div>
          <div>
            <div className="text-base font-bold tracking-tight text-[var(--color-ink)]">
              Health Data Distributions
            </div>
            <div className="text-xs text-[var(--color-ink-muted)]">
              Empirical Reference Norms for Study Sizing &amp; Device Validation
            </div>
          </div>
        </button>

        {/* Center Nav Tabs */}
        <nav className="hidden md:flex items-center gap-1 rounded-xl border border-[var(--color-grid)] bg-[var(--color-surface-subtle)] p-1 text-xs">
          <button
            type="button"
            onClick={() => {
              onTabChange('catalog');
              onSelectMetric?.(null);
            }}
            className={`rounded-lg px-3 py-1.5 font-semibold transition-all ${
              activeTab === 'catalog'
                ? 'bg-[var(--color-surface)] text-[var(--color-ink)] shadow-xs'
                : 'text-[var(--color-ink-secondary)] hover:text-[var(--color-ink)]'
            }`}
          >
            Catalog
          </button>
          <button
            type="button"
            onClick={() => {
              onTabChange('divergence');
              onSelectMetric?.(null);
            }}
            className={`flex items-center gap-1.5 rounded-lg px-3 py-1.5 font-semibold transition-all ${
              activeTab === 'divergence'
                ? 'bg-[var(--color-surface)] text-[var(--color-warning)] shadow-xs'
                : 'text-[var(--color-ink-secondary)] hover:text-[var(--color-ink)]'
            }`}
          >
            <GitFork className="h-3.5 w-3.5" />
            <span>Method Matters</span>
          </button>
          <button
            type="button"
            onClick={() => {
              onTabChange('wizard');
              onSelectMetric?.(null);
            }}
            className={`flex items-center gap-1.5 rounded-lg px-3 py-1.5 font-semibold transition-all ${
              activeTab === 'wizard'
                ? 'bg-[var(--color-surface)] text-[var(--color-series-1)] shadow-xs'
                : 'text-[var(--color-ink-secondary)] hover:text-[var(--color-ink)]'
            }`}
          >
            <HelpCircle className="h-3.5 w-3.5" />
            <span>Fit-for-Purpose</span>
          </button>
        </nav>

        {/* External links & Theme Toggle */}
        <div className="flex items-center gap-3 sm:gap-4">
          <a
            href="https://ross-wilkinson.github.io/validation-study-designer/#/curriculum"
            target="_blank"
            rel="noreferrer"
            className="hidden items-center gap-1.5 rounded-md px-2.5 py-1.5 text-xs font-semibold text-[var(--color-series-1)] bg-[var(--color-series-1)]/10 hover:bg-[var(--color-series-1)]/15 transition-colors sm:inline-flex"
            title="Validation Academy Curriculum"
          >
            <GraduationCap className="h-3.5 w-3.5" />
            <span>Validation Academy</span>
            <ExternalLink className="h-3 w-3 opacity-70" />
          </a>

          <button
            type="button"
            onClick={toggleTheme}
            aria-label="Toggle theme"
            className="flex h-8 w-8 items-center justify-center rounded-md border border-[var(--color-grid)] bg-[var(--color-surface)] text-[var(--color-ink-secondary)] hover:bg-[var(--color-surface-subtle)] hover:text-[var(--color-ink)] transition-colors"
          >
            {theme === 'dark' ? <Sun className="h-4 w-4" /> : <Moon className="h-4 w-4" />}
          </button>
        </div>
      </div>
    </header>
  );
};
