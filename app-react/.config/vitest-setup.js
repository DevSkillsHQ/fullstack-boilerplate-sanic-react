import {afterEach, vi} from 'vitest';

// runs a cleanup after each test case (e.g. clearing jsdom)
afterEach(() => {
    vi.clearAllTimers();
    vi.clearAllMocks();
});
