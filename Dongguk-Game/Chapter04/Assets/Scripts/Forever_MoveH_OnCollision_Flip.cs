using System.Collections;
using System.Collections.Generic;
using UnityEngine;

// ��� �̵��ϰ�, �浹�ϸ� �����Ѵ�(����)
public class Forever_MoveH_OnCollision_Flip : MonoBehaviour
{

    public float speed = 1; // �ӵ�: Inspector�� ����

    Rigidbody2D rbody;

    // Start is called before the first frame update
    void Start()    // ó���� �����Ѵ�
    {
        // �߷��� 0���� �ؼ� �浹 �ÿ� ȸ����Ű�� �ʴ´�
        rbody = GetComponent<Rigidbody2D>();
        rbody.gravityScale = 0;
        rbody.constraints = RigidbodyConstraints2D.FreezeRotation;
    }

    private void FixedUpdate()  // ��� �����Ѵ�(���� �ð�����)
    {
        // �������� �̵��Ѵ�
        rbody.velocity = new Vector2(speed, 0);
    }

    private void OnCollisionEnter2D(Collision2D collision)  // �浹���� ��
    {
        speed = -speed; // ���ư��� ������ ������Ų��
                        // ���ư��� ���⿡�� ���� �������� ������ �ٲ۴�
        this.GetComponent<SpriteRenderer>().flipX = (speed < 0);
    }

}
