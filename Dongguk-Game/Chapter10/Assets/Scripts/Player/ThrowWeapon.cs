using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ThrowWeapon : MonoBehaviour
{
    [SerializeField] private GameObject weapon;
    [SerializeField] private KeyCode[] keys;
    public float cooldownTime = 2f;
    private bool canUseAbility = true;
    public float deleteTime = 3f;


    public float throwX = 4;
    public float throwY = 8;
    public float offsetY = 1;

    private bool leftFlag = false;


    private void Update()
    {
        if (Input.GetKey(keys[0]))
        {
            leftFlag = true;
        }
        if (Input.GetKey(keys[1]))
        {
            leftFlag= false;
        }
        if (canUseAbility && Input.GetKeyDown(keys[2]))
        {
            canUseAbility = false; // �ɷ� ��� ���̹Ƿ� ��� �Ұ��� ���·� ����

            StartCoroutine(EnableAbilityAfterCooldown()); // ��Ÿ�� ���Ŀ� �ɷ� ��� ������ ���·� �����ϴ� �ڷ�ƾ ����

            Vector3 area = this.GetComponent<SpriteRenderer>().bounds.size;
            Vector3 newPos = this.transform.position;
            newPos.y += offsetY;

            GameObject newGameObject = Instantiate(weapon) as GameObject;
            StartCoroutine(DestroyPrefab(newGameObject, deleteTime));
            newPos.z = -5;
            newGameObject.GetComponent<SpriteRenderer>().flipX = leftFlag;
            newGameObject.transform.position = newPos;

            Rigidbody2D r2d = newGameObject.GetComponent<Rigidbody2D>();

            if (leftFlag)
            {
                r2d.AddForce(new Vector2(-throwX, throwY), ForceMode2D.Impulse);
            }
            else
            {
                r2d.AddForce(new Vector2(throwX, throwY), ForceMode2D.Impulse);
            }
        }
    }

    private IEnumerator DestroyPrefab(GameObject prefab, float delay)
    {
        yield return new WaitForSeconds(delay);
        Destroy(prefab);
    }

    private IEnumerator EnableAbilityAfterCooldown()
    {
        yield return new WaitForSeconds(cooldownTime);
        canUseAbility = true; // ��Ÿ�� ���Ŀ� �ɷ� ��� ������ ���·� ����
    }
}
