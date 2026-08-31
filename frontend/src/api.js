const API_TIMEOUT_MS = 8000;

export async function apiFetch(path, options = {}) {
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), API_TIMEOUT_MS);
  try {
    const response = await fetch(path, {
      ...options,
      headers: {
        Accept: "application/json",
        ...(options.body ? { "Content-Type": "application/json" } : {}),
        ...(options.headers || {}),
      },
      signal: controller.signal,
    });
    let data = null;
    try {
      data = await response.json();
    } catch {
      data = null;
    }
    if (!response.ok) {
      const message =
        (data && data.error) ||
        `Request failed (${response.status}). Nothing was saved.`;
      const error = new Error(message);
      error.status = response.status;
      error.code = data && data.code;
      error.data = data;
      throw error;
    }
    return data;
  } catch (err) {
    if (err.name === "AbortError") {
      throw new Error("The request timed out. Nothing was saved.");
    }
    throw err;
  } finally {
    clearTimeout(timer);
  }
}
