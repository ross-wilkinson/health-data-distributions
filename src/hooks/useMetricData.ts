import { useState, useEffect } from 'react';
import type { CatalogPayload, MetricDetail } from '../types/metric';

const metricCache = new Map<string, MetricDetail>();
let catalogCache: CatalogPayload | null = null;

export function useCatalog() {
  const [data, setData] = useState<CatalogPayload | null>(catalogCache);
  const [loading, setLoading] = useState<boolean>(!catalogCache);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (catalogCache) {
      setData(catalogCache);
      setLoading(false);
      return;
    }

    let isMounted = true;
    fetch('./data/catalog.json')
      .then((res) => {
        if (!res.ok) {
          throw new Error(`Failed to load catalog (${res.status} ${res.statusText})`);
        }
        return res.json();
      })
      .then((json: CatalogPayload) => {
        if (isMounted) {
          catalogCache = json;
          setData(json);
          setLoading(false);
        }
      })
      .catch((err: Error) => {
        if (isMounted) {
          setError(err.message);
          setLoading(false);
        }
      });

    return () => {
      isMounted = false;
    };
  }, []);

  return { data, loading, error };
}

export function useMetric(metricId: string | null) {
  const [data, setData] = useState<MetricDetail | null>(metricId ? metricCache.get(metricId) ?? null : null);
  const [loading, setLoading] = useState<boolean>(metricId ? !metricCache.has(metricId) : false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (!metricId) {
      setData(null);
      setLoading(false);
      return;
    }

    if (metricCache.has(metricId)) {
      setData(metricCache.get(metricId)!);
      setLoading(false);
      return;
    }

    let isMounted = true;
    setLoading(true);
    setError(null);

    fetch(`./data/metrics/${metricId}.json`)
      .then((res) => {
        if (!res.ok) {
          throw new Error(`Failed to load metric ${metricId} (${res.status})`);
        }
        return res.json();
      })
      .then((json: MetricDetail) => {
        if (isMounted) {
          metricCache.set(metricId, json);
          setData(json);
          setLoading(false);
        }
      })
      .catch((err: Error) => {
        if (isMounted) {
          setError(err.message);
          setLoading(false);
        }
      });

    return () => {
      isMounted = false;
    };
  }, [metricId]);

  return { data, loading, error };
}
