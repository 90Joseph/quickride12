import React from 'react';
import { Platform } from 'react-native';

// Platform-specific navigation implementation
// Web uses Google Maps JS API, Native uses react-native-maps

let RiderNavigationComponent: any;

if (Platform.OS === 'web') {
  // Web implementation with Google Maps JavaScript API
  RiderNavigationComponent = require('./navigation.web').default;
} else {
  // Native implementation with react-native-maps
  RiderNavigationComponent = require('./navigation.native').default;
}

export default function RiderNavigationScreen() {
  return <RiderNavigationComponent />;
}
