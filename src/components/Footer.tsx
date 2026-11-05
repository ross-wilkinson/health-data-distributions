import React from 'react';
import { ShieldCheck, BookOpen, Layers } from 'lucide-react';

export const Footer: React.FC = () => {
  return (
    <footer className="border-t border-[var(--color-grid)] bg-[var(--color-surface)] py-12 transition-colors">
      <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
        <div className="grid grid-cols-1 gap-8 md:grid-cols-3">
          <div>
            <div className="flex items-center gap-2 text-sm font-bold text-[var(--color-ink)]">
              <ShieldCheck className="h-4 w-4 text-[var(--color-series-1)]" />
              <span>Epistemological Invariants</span>
            </div>
            <p className="mt-2 text-xs leading-relaxed text-[var(--color-ink-muted)]">
              Every distribution is traceable directly to an open pipeline or a verbatim primary
              literature citation. Measurement method is part of the data: disparate protocols are never
              pooled. No algorithmic whitewashing via Bayesian hierarchical shrinkage across melanin classes.
            </p>
          </div>

          <div>
            <div className="flex items-center gap-2 text-sm font-bold text-[var(--color-ink)]">
              <Layers className="h-4 w-4 text-[var(--color-series-2)]" />
              <span>Validation Ecosystem</span>
            </div>
            <ul className="mt-2 space-y-1 text-xs text-[var(--color-ink-muted)]">
              <li>
                <a
                  href="https://ross-wilkinson.github.io/validation-study-designer/"
                  target="_blank"
                  rel="noreferrer"
                  className="hover:text-[var(--color-ink)] underline"
                >
                  Validation Study Designer (Study Sizing &amp; Quotas)
                </a>
              </li>
              <li>
                <a
                  href="https://github.com/ross-wilkinson/agreekit"
                  target="_blank"
                  rel="noreferrer"
                  className="hover:text-[var(--color-ink)] underline"
                >
                  agreekit (Closed-Form ANOVA &amp; Agreement Statistics)
                </a>
              </li>
              <li>
                <a
                  href="https://ross-wilkinson.github.io/validation-study-designer/#/curriculum"
                  target="_blank"
                  rel="noreferrer"
                  className="hover:text-[var(--color-ink)] underline"
                >
                  Validation Academy (Meridian Biosystems Case Studies)
                </a>
              </li>
            </ul>
          </div>

          <div>
            <div className="flex items-center gap-2 text-sm font-bold text-[var(--color-ink)]">
              <BookOpen className="h-4 w-4 text-[var(--color-series-3)]" />
              <span>Zero-Lock-in Open Science</span>
            </div>
            <p className="mt-2 text-xs leading-relaxed text-[var(--color-ink-muted)]">
              All datasets and distributions are statically queryable via JSON API endpoints and tidy CSV exports.
              Citable BibTeX blocks provided for every primary source to satisfy FDA 510(k), ISO 80601-2-61, and IRB submissions.
            </p>
          </div>
        </div>

        <div className="mt-8 border-t border-[var(--color-grid)] pt-6 text-center text-xs text-[var(--color-ink-muted)]">
          Health Data Distributions &bull; Open-source population health statistics for medical device and algorithm validation.
        </div>
      </div>
    </footer>
  );
};
