import { View, Text, TouchableOpacity, StyleSheet } from 'react-native';

export default function ErrorMessage({ message, onRetry, icon = '' }) {
   return (
      <View style={styles.container}>
         <Text style={styles.icon}>{icon}</Text>
         <Text style={styles.title}>Ops! Algo deu errado</Text>
         <Text style={styles.message}>{message}</Text>

         {onRetry && (
            <TouchableOpacity style={styles.button} onPress={onRetry}>
               <Text style={styles.buttonText}>Tentar Novamente</Text>
            </TouchableOpacity>
         )}
      </View>
   );
}

const styles = StyleSheet.create({
   container: {
      flex: 1,
      justifyContent: 'center',
      alignItems: 'center',
      backgroundColor: '#f5f5f5',
      padding: 20,
   },
   icon: {
      fontSize: 64,
      marginBottom: 10,
   },
   title: {
      fontSize: 22,
      fontWeight: 'bold',
      color: '#333',
      marginBottom: 10,
   },
   message: {
      fontSize: 16,
      color: '#666',
      textAlign: 'center',
      marginBottom: 30,
   },
   button: {
      backgroundColor: '#007AFF',
      paddingHorizontal: 30,
      paddingVertical: 15,
      borderRadius: 8,
   },
   buttonText: {
      color: '#fff',
      fontSize: 16,
      fontWeight: '600',
   },
});
