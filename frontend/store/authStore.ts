import { create } from 'zustand';
import { Platform } from 'react-native';

// Platform-specific storage
const storage = {
  async getItem(key: string): Promise<string | null> {
    if (Platform.OS === 'web') {
      return localStorage.getItem(key);
    } else {
      const AsyncStorage = require('@react-native-async-storage/async-storage').default;
      return await AsyncStorage.getItem(key);
    }
  },
  async setItem(key: string, value: string): Promise<void> {
    if (Platform.OS === 'web') {
      localStorage.setItem(key, value);
    } else {
      const AsyncStorage = require('@react-native-async-storage/async-storage').default;
      await AsyncStorage.setItem(key, value);
    }
  },
  async removeItem(key: string): Promise<void> {
    if (Platform.OS === 'web') {
      localStorage.removeItem(key);
    } else {
      const AsyncStorage = require('@react-native-async-storage/async-storage').default;
      await AsyncStorage.removeItem(key);
    }
  },
};

interface User {
  id: string;
  email: string;
  name: string;
  picture?: string;
  role: 'customer' | 'restaurant' | 'rider' | 'admin';
  phone?: string;
}

interface AuthStore {
  user: User | null;
  sessionToken: string | null;
  isLoading: boolean;
  setUser: (user: User | null) => void;
  setSessionToken: (token: string | null) => void;
  setLoading: (loading: boolean) => void;
  logout: () => void;
  initializeAuth: () => Promise<void>;
}

export const useAuthStore = create<AuthStore>((set) => ({
  user: null,
  sessionToken: null,
  isLoading: true,
  setUser: (user) => {
    set({ user });
    if (user) {
      AsyncStorage.setItem('user', JSON.stringify(user));
    } else {
      AsyncStorage.removeItem('user');
    }
  },
  setSessionToken: (token) => {
    set({ sessionToken: token });
    if (token) {
      AsyncStorage.setItem('sessionToken', token);
    } else {
      AsyncStorage.removeItem('sessionToken');
    }
  },
  setLoading: (loading) => set({ isLoading: loading }),
  logout: () => {
    set({ user: null, sessionToken: null });
    AsyncStorage.removeItem('user');
    AsyncStorage.removeItem('sessionToken');
  },
  initializeAuth: async () => {
    try {
      const [storedToken, storedUser] = await Promise.all([
        AsyncStorage.getItem('sessionToken'),
        AsyncStorage.getItem('user'),
      ]);

      if (storedToken && storedUser) {
        set({
          sessionToken: storedToken,
          user: JSON.parse(storedUser),
        });
      }
    } catch (error) {
      console.error('Error initializing auth:', error);
    } finally {
      set({ isLoading: false });
    }
  },
}));
