import { create } from 'zustand';
import AsyncStorage from '@react-native-async-storage/async-storage';

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
