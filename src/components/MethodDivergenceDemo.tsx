import React, { useState } from 'react';
import { AlertTriangle, GitFork, ShieldAlert } from 'lucide-react';

export const MethodDivergenceDemo: React.FC = () => {
  const [showPooled, setShowPooled] = useState<boolean>(false);

  // Generate normal distribution curve points
  const generateCurve = (mean: number, sd: number, points = 60, min = 40, max = 110) => {
    const step = (max - min) / points;
    const pts: { x: number; y: number }[] = [];
    const normFactor = 1 / (sd * Math.sqrt(2 * Math.PI));
    for (let x = min; x <= max; x += step) {
      const exponent = -0.5 * Math.pow((x - mean) / sd, 2);
      const y = normFactor * Math.exp(exponent);
      pts.push({ x: Math.round(x * 10) / 10, y });
    }
    return pts;
  };

  const nhanesCurve = generateCurve(72.41, 11.69); // Clinic
  const fitbitCurve = generateCurve(65.5, 7.7);   // Wearable

  // Naive pooled mixture (equal weight for demonstration)
  const pooledCurve = nhanesCurve.map((pt, i) => ({
    x: pt.x,
    y: (pt.y + (fitbitCurve[i]?.y ?? 0)) / 2,
  }));

  const maxDensity = Math.max(...fitbitCurve.map((p) => p.y));

  // SVG viewBox width/height
  const w = 600;
  const h = 200;
  const padX = 40;
  const padY = 20;

  const scaleX = (val: number) => padX + ((val - 40) / 70) * (w - 2 * padX);
  const scaleY = (density: number) => h - padY - (density / maxDensity) * (h - 2 * padY);

  const createPathD = (pts: { x: number; y: number }[]) => {
    return pts.reduce((acc, pt, i) => {
      const x = scaleX(pt.x);
      const y = scaleY(pt.y);
      return `${acc} ${i === 0 ? 'M' : 'L'} ${x} ${y}`;
    }, '');
  };

  const createAreaD = (pts: { x: number; y: number }[]) => {
    const lineD = createPathD(pts);
    const firstX = scaleX(pts[0]!.x);
    const lastX = scaleX(pts[pts.length - 1]!.x);
    const baseY = h - padY;
    return `${lineD} L ${lastX} ${baseY} L ${firstX} ${baseY} Z`;
  };

  return (
    <div className="rounded-2xl border border-[var(--color-grid)] bg-[var(--color-surface)] p-6 sm:p-8 shadow-xs space-y-6">
      <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4 border-b border-[var(--color-grid)] pb-5">
        <div>
          <div className="inline-flex items-center gap-1.5 rounded-md bg-[var(--color-warning)]/10 px-2 py-0.5 text-xs font-bold text-[var(--color-warning)]">
            <GitFork className="h-3.5 w-3.5" />
            <span>Interactive Epistemology Demonstrator</span>
          </div>
          <h2 className="mt-2 text-xl font-black tracking-tight text-[var(--color-ink)]">
            Why Measurement Method is Part of the Data
          </h2>
          <p className="mt-1 text-xs text-[var(--color-ink-secondary)]">
            Contrast the empirical distributions of NHANES Seated Clinic Pulse vs. Quer et al. Fitbit Wearable Resting HR.
          </p>
        </div>

        <button
          type="button"
          onClick={() => setShowPooled(!showPooled)}
          className={`inline-flex items-center gap-2 rounded-xl px-4 py-2 text-xs font-bold transition-all shadow-xs ${
            showPooled
              ? 'bg-[var(--color-critical)] text-white hover:opacity-90 ring-2 ring-[var(--color-critical)]/30'
              : 'border border-[var(--color-grid)] bg-[var(--color-surface-subtle)] text-[var(--color-ink)] hover:bg-[var(--color-surface)]'
          }`}
        >
          <AlertTriangle className="h-4 w-4" />
          <span>{showPooled ? 'Show Distinct Distributions' : 'Simulate Naïve Pooling'}</span>
        </button>
      </div>

      {/* Metric Comparison Cards */}
      <div className="grid grid-cols-1 gap-4 sm:grid-cols-2">
        <div className="rounded-xl border border-[var(--color-series-1)]/30 bg-[var(--color-series-1)]/5 p-4 text-xs">
          <div className="flex items-center justify-between">
            <span className="font-bold text-[var(--color-series-1)]">NHANES 2015–2018</span>
            <span className="rounded bg-[var(--color-series-1)]/10 px-1.5 py-0.5 font-mono text-[10px] text-[var(--color-series-1)]">
              Clinic Auscultation
            </span>
          </div>
          <div className="mt-2 text-2xl font-black font-mono text-[var(--color-ink)]">
            72.4 <span className="text-sm font-normal text-[var(--color-ink-muted)]">bpm</span>
          </div>
          <div className="mt-1 text-[var(--color-ink-secondary)]">
            Between-Subject &sigma;<sub>b</sub> = <strong>11.7 bpm</strong> &bull; n = 10,848 (Weighted)
          </div>
          <p className="mt-2 text-[11px] text-[var(--color-ink-muted)] leading-relaxed">
            30-second seated pulse counted by trained examiner after 5 min quiet rest during a daytime exam clinic.
          </p>
        </div>

        <div className="rounded-xl border border-[var(--color-series-2)]/30 bg-[var(--color-series-2)]/5 p-4 text-xs">
          <div className="flex items-center justify-between">
            <span className="font-bold text-[var(--color-series-2)]">Quer et al. 2020 (Fitbit)</span>
            <span className="rounded bg-[var(--color-series-2)]/10 px-1.5 py-0.5 font-mono text-[10px] text-[var(--color-series-2)]">
              Continuous Wearable
            </span>
          </div>
          <div className="mt-2 text-2xl font-black font-mono text-[var(--color-series-2)]">
            65.5 <span className="text-sm font-normal text-[var(--color-ink-muted)]">bpm</span>
          </div>
          <div className="mt-1 text-[var(--color-ink-secondary)]">
            Between-Subject &sigma;<sub>b</sub> = <strong>7.7 bpm</strong> &bull; n = 92,457 (Longitudinal)
          </div>
          <p className="mt-2 text-[11px] text-[var(--color-ink-muted)] leading-relaxed">
            Multi-day longitudinal subject average derived from proprietary PPG algorithm during sleep and supine waking.
          </p>
        </div>
      </div>

      {/* SVG Density Curve Visualizer */}
      <div className="rounded-xl border border-[var(--color-grid)] bg-[var(--color-plane)] p-4 sm:p-6">
        <div className="flex flex-wrap items-center justify-between gap-2 text-xs mb-4">
          <div className="font-bold text-[var(--color-ink)]">
            {showPooled ? (
              <span className="text-[var(--color-critical)] font-bold flex items-center gap-1.5">
                <ShieldAlert className="h-4 w-4" />
                Naïve Mixture: Bimodal Artifact with Artificially Inflated Variance
              </span>
            ) : (
              <span>Empirical Probability Density Curves: Notice the 6.9 bpm Offset</span>
            )}
          </div>
          <div className="flex items-center gap-4 text-[11px]">
            {!showPooled ? (
              <>
                <div className="flex items-center gap-1.5">
                  <div className="h-2.5 w-2.5 rounded-full bg-[var(--color-series-1)]" />
                  <span className="text-[var(--color-ink-secondary)]">Clinic (72.4 bpm)</span>
                </div>
                <div className="flex items-center gap-1.5">
                  <div className="h-2.5 w-2.5 rounded-full bg-[var(--color-series-2)]" />
                  <span className="text-[var(--color-ink-secondary)]">Wearable (65.5 bpm)</span>
                </div>
              </>
            ) : (
              <div className="flex items-center gap-1.5">
                <div className="h-2.5 w-2.5 rounded-full bg-[var(--color-critical)]" />
                <span className="font-bold text-[var(--color-critical)]">Pooled Chimera Distribution</span>
              </div>
            )}
          </div>
        </div>

        <div className="w-full overflow-hidden">
          <svg viewBox={`0 0 ${w} ${h}`} className="w-full h-auto select-none">
            {/* Grid baseline */}
            <line x1={padX} y1={h - padY} x2={w - padX} y2={h - padY} stroke="var(--color-grid)" strokeWidth="1" />

            {/* X-axis ticks */}
            {[40, 50, 60, 70, 80, 90, 100, 110].map((bpm) => {
              const x = scaleX(bpm);
              return (
                <g key={bpm}>
                  <line x1={x} y1={h - padY} x2={x} y2={h - padY + 4} stroke="var(--color-axis)" strokeWidth="1" />
                  <text x={x} y={h - padY + 14} textAnchor="middle" fontSize="9" fill="var(--color-ink-muted)" fontFamily="var(--font-mono)">
                    {bpm}
                  </text>
                </g>
              );
            })}

            {!showPooled ? (
              <>
                {/* Wearable Area & Line */}
                <path d={createAreaD(fitbitCurve)} fill="var(--color-series-2)" fillOpacity="0.15" />
                <path d={createPathD(fitbitCurve)} fill="none" stroke="var(--color-series-2)" strokeWidth="2.5" />

                {/* Clinic Area & Line */}
                <path d={createAreaD(nhanesCurve)} fill="var(--color-series-1)" fillOpacity="0.15" />
                <path d={createPathD(nhanesCurve)} fill="none" stroke="var(--color-series-1)" strokeWidth="2.5" />

                {/* Mean markers */}
                <line
                  x1={scaleX(65.5)}
                  y1={scaleY(maxDensity * 0.95)}
                  x2={scaleX(65.5)}
                  y2={h - padY}
                  stroke="var(--color-series-2)"
                  strokeWidth="1.5"
                  strokeDasharray="3 3"
                />
                <line
                  x1={scaleX(72.41)}
                  y1={scaleY(maxDensity * 0.7)}
                  x2={scaleX(72.41)}
                  y2={h - padY}
                  stroke="var(--color-series-1)"
                  strokeWidth="1.5"
                  strokeDasharray="3 3"
                />
              </>
            ) : (
              <>
                {/* Pooled Chimera Area & Line */}
                <path d={createAreaD(pooledCurve)} fill="var(--color-critical)" fillOpacity="0.2" />
                <path d={createPathD(pooledCurve)} fill="none" stroke="var(--color-critical)" strokeWidth="3" />
                <line
                  x1={scaleX(68.9)}
                  y1={scaleY(maxDensity * 0.65)}
                  x2={scaleX(68.9)}
                  y2={h - padY}
                  stroke="var(--color-critical)"
                  strokeWidth="2"
                  strokeDasharray="4 4"
                />
              </>
            )}
          </svg>
        </div>

        {/* Dynamic Analysis Callout */}
        <div className="mt-4 rounded-lg bg-[var(--color-surface)] p-3 border border-[var(--color-grid)] text-xs">
          {showPooled ? (
            <div className="space-y-1.5 text-[var(--color-ink-secondary)]">
              <div className="font-bold text-[var(--color-critical)]">
                The Consequence of Naïve Pooling:
              </div>
              <div>
                Merging these datasets creates an artifactual distribution that describes <em>neither</em> clinical auscultation <em>nor</em> wearable tracking.
                The between-subject variance is artificially inflated (&sigma;<sub>b</sub> increases from 7.7 to 10.2+ bpm), falsely ballooning sample size calculations in study design by over <strong>75%</strong>!
              </div>
            </div>
          ) : (
            <div className="space-y-1 text-[var(--color-ink-secondary)]">
              <div className="font-bold text-[var(--color-ink)]">
                The 6.9 bpm Discrepancy Explained:
              </div>
              <div>
                Seated clinic exams introduce sympathetic autonomic tone (white-coat reactivity), posture effects, and discrete 30-second integer quantization. Wearables record basal supine rates on waking. These are distinct biological variables.
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};
