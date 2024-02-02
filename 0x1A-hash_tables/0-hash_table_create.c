#include "hash_tables.h"

/**
 * hash_table_create - This is a function that creates a hash table
 * @size: The size of the hash table
 *
 * Return: A pointer to the newly created hash table
  */

hash_table_t *hash_table_create(unsigned long int size)
{
	unsigned long int i = 0;
	hash_table_t *ht;

	ht = malloc(sizeof(hash_table_t));
	if (ht == NULL)
	{
		free(ht);
		return (NULL);
	}

	ht->array = malloc(sizeof(hash_node_t *) * size);
	if (ht->array == NULL)
	{
		free(ht);
		return (NULL);
	}
	for (i = 0; i < size; i++)
	{
		ht->array[i] = NULL;
	}

	return (ht);
}
