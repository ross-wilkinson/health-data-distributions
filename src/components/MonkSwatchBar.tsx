import React from 'react';

export const MONK_PALETTE = [
  { tone: 'Monk 1', hex: '#f6ede4', textDark: true },
  { tone: 'Monk 2', hex: '#f3e7db', textDark: true },
  { tone: 'Monk 3', hex: '#f7ead0', textDark: true },
  { tone: 'Monk 4', hex: '#eadaba', textDark: true },
  { tone: 'Monk 5', hex: '#d7bd96', textDark: true },
  { tone: 'Monk 6', hex: '#a07e56', textDark: false },
  { tone: 'Monk 7', hex: '#825c43', textDark: false },
  { tone: 'Monk 8', hex: '#604134', textDark: false },
  { tone: 'Monk 9', hex: '#3a312a', textDark: false },
  { tone: 'Monk 10', hex: '#292420', textDark: false },
];

interface MonkSwatchBarProps {
  shares?: Record<string, number>;
  activeTone?: string | null;
  onSelectTone?: (tone: string) => void;
}

export const MonkSwatchBar: React.FC<MonkSwatchBarProps> = ({
  shares,
  activeTone,
  onSelectTone,
}) => {
  return (
    <div className="rounded-xl border border-[var(--color-grid)] bg-[var(--color-surface)] p-4 shadow-xs">
      <div className="mb-3 flex items-center justify-between">
        <div>
          <div className="text-xs font-bold uppercase tracking-wider text-[var(--color-ink-muted)]">
            Monk Skin Tone Scale (MST 1–10)
          </div>
          <div className="text-xs text-[var(--color-ink-secondary)]">
            Calibrated 10-shade standard designed to eliminate skin tone bias in optical and digital imaging
          </div>
        </div>
      </div>

      <div className="grid grid-cols-5 gap-2 sm:grid-cols-10">
        {MONK_PALETTE.map((item, idx) => {
          const num = idx + 1;
          const share = shares ? shares[`Monk ${num}`] ?? shares[`${num}`] : null;
          const isSelected = activeTone === item.tone || activeTone === `Monk ${num}`;

          return (
            <button
              key={item.tone}
              type="button"
              onClick={() => onSelectTone?.(item.tone)}
              className={`group flex flex-col items-center rounded-lg border p-2 transition-all ${
                isSelected
                  ? 'border-[var(--color-series-1)] ring-2 ring-[var(--color-series-1)]/30'
                  : 'border-[var(--color-grid)] hover:border-[var(--color-ink-muted)]'
              }`}
            >
              <div
                className="h-10 w-full rounded-md shadow-xs border border-black/10 transition-transform group-hover:scale-105"
                style={{ backgroundColor: item.hex }}
              />
              <div className="mt-2 text-center">
                <div className="text-[11px] font-bold text-[var(--color-ink)]">{num}</div>
                <div className="text-[9px] font-mono text-[var(--color-ink-muted)]">{item.hex}</div>
                {share != null && (
                  <div className="mt-1 text-[10px] font-semibold text-[var(--color-series-1)]">
                    {(share * 100).toFixed(1)}%
                  </div>
                )}
              </div>
            </button>
          );
        })}
      </div>
    </div>
  );
};
