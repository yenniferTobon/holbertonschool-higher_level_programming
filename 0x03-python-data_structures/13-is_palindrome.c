#include "lists.h"

/**
* is_palindrome - Function that checks if a list is palindrome
* @head: The start
* Return: The integer value
*/
int is_palindrome(listint_t **head)
{
listint_t *temp = *head;
int buff[1000];
int i = 0;
int j = 0;
int size = 0;

	if (head == NULL)
		return (1);

	if (temp->next == NULL)
		return (1);

	if (*head == NULL)
		return (1);

	while (temp != NULL)
	{
		buff[i] = temp->n;
		temp = temp->next;
		i++;
	}
	size = i - 1;
	while (j <= size)
	{
		if (buff[size] != buff[j])
			return (0);
		size--;
		j++;
	}
	return (1);
}
