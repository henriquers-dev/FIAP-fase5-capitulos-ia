import { View, ActivityIndicator, Text, StyleSheet } from 'react-native';
export default function LoadingSpinner({ message = 'Carregando...', size = 'large' }) {
   return (
      <View style={styles.container}>
         <ActivityIndicator size={size} color="#E63946" />
         {message && <Text style={styles.message}>{message}</Text>}
      </View>
   );
}

const styles = StyleSheet.create({
   container: {
      flex: 1,
      justifyContent: 'center',
      alignItems: 'center',
      backgroundColor: '#f5f5f5',
   },
   message: {
      marginTop: 15,
      fontSize: 16,
      color: '#666',
      textAlign: 'center',
   },
});
